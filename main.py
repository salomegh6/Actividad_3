from sqlalchemy import create_engine, text, URL
from dotenv import load_dotenv
from faker import Faker
import os


# Funcion para crear la tabla.
def crear_tabla(conn):

    query = """
    CREATE TABLE IF NOT EXISTS personas_salome (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre_completo VARCHAR(100),
        fecha_nacimiento DATE,
        correo_electronico VARCHAR(100) UNIQUE,
        telefono VARCHAR(50) UNIQUE,
        ciudad VARCHAR(100),
        direccion VARCHAR(200),
        estado_civil VARCHAR(100),
        ocupacion VARCHAR(100)
    );
    """

    # Ejecutar la consulta.
    conn.execute(text(query))


# Funcion para insertar los datos.
def insertar_datos(conn, rows):

    query = text("""
        INSERT INTO personas_salome (
            nombre_completo,
            fecha_nacimiento,
            correo_electronico,
            telefono,
            ciudad,
            direccion,
            estado_civil,
            ocupacion
        )
        VALUES (
            :nombre_completo,
            :fecha_nacimiento,
            :correo_electronico,
            :telefono,
            :ciudad,
            :direccion,
            :estado_civil,
            :ocupacion
        )
    """)

    # Insertar los registros del grupo.
    conn.execute(query, rows)


# Funcion principal del programa.
def main():

    # Cargar los datos del archivo .env.
    load_dotenv()

    # Obtener los datos de conexion a MySQL.
    usuario = os.getenv("DB_USER")
    contrasena = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    puerto = int(os.getenv("DB_PORT", "3306"))
    base_datos = os.getenv("DB_NAME")

    # Comprobar que los datos necesarios existan.
    if not all([usuario, contrasena, host, base_datos]):
        print("Error: revisa las variables de conexion en el archivo .env")
        return

    try:

        # Preparar la conexion con MySQL.
        url = URL.create(
            "mysql+pymysql",
            username=usuario,
            password=contrasena,
            host=host,
            port=puerto,
            database=base_datos
        )

        # Crear el motor de conexion.
        engine = create_engine(url)

        # Crear los datos ficticios en español.
        fake = Faker("es_ES")

        # Abrir la conexion y comenzar una transaccion.
        with engine.begin() as conn:

            # Comprobar que la conexion funciona.
            conn.execute(text("SELECT 1"))
            print("Conexion exitosa con MySQL")

            # Crear la tabla si todavia no existe.
            crear_tabla(conn)
            print("Tabla creada correctamente")

            # Contar los registros que ya existen.
            cantidad = conn.execute(
                text("SELECT COUNT(*) FROM personas_salome")
            ).scalar_one()

            # Evitar insertar otros 100000 registros por accidente.
            if cantidad == 100000:
                print("La tabla ya contiene 100000 registros.")
                print("No se insertaron registros adicionales.")

            else:
                # Si hay registros anteriores, limpiar esta tabla.
                conn.execute(text("DELETE FROM personas_salome"))

                # Definir la cantidad de personas que se van a generar.
                total = 100000

                # Definir el tamano de cada grupo.
                tamano_grupo = 1000

                # Generar e insertar los datos por grupos.
                for inicio in range(0, total, tamano_grupo):

                    # Crear una lista vacia para el grupo.
                    rows = []

                    # Generar los datos ficticios.
                    for _ in range(tamano_grupo):

                        # Crear los datos de una persona.
                        persona = {
                            "nombre_completo": fake.name(),
                            "fecha_nacimiento": fake.date_of_birth(
                                minimum_age=18,
                                maximum_age=90
                            ),
                            "correo_electronico": fake.unique.email(),
                            "telefono": fake.unique.phone_number(),
                            "ciudad": fake.city(),
                            "direccion": fake.address(),
                            "estado_civil": fake.random_element(
                                elements=[
                                    "Soltero",
                                    "Casado",
                                    "Divorciado",
                                    "Viudo"
                                ]
                            ),
                            "ocupacion": fake.job()
                        }

                        # Agregar la persona al grupo.
                        rows.append(persona)

                    # Insertar el grupo en MySQL.
                    insertar_datos(conn, rows)

                    # Mostrar el progreso.
                    print(
                        f"Registros procesados: "
                        f"{inicio + tamano_grupo} de {total}"
                    )

        # Consultar la cantidad final de registros.
        with engine.connect() as conn:
            cantidad_final = conn.execute(
                text("SELECT COUNT(*) FROM personas_salome")
            ).scalar_one()

        # Mostrar el resultado final.
        print("Proceso terminado.")
        print("Total de personas en la tabla:", cantidad_final)

        # Cerrar el motor de conexion.
        engine.dispose()

    except Exception as e:
        print("Error al ejecutar el programa:")
        print(e)


# Ejecutar el programa.
if __name__ == "__main__":
    main()
