
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text, URL


def main():
    # Leer las variables del archivo .env
    load_dotenv()

    # Obtener los datos de conexión
    usuario = os.getenv("DB_USER")
    contrasena = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    puerto = int(os.getenv("DB_PORT"))
    base_datos = os.getenv("DB_NAME")

    # Preparar la conexión con MySQL
    url = URL.create(
        "mysql+pymysql",
        username=usuario,
        password=contrasena,
        host=host,
        port=puerto,
        database=base_datos
    )

    # Crear el motor de conexión
    motor = create_engine(url)

    # Comprobar si la conexión funciona
    with motor.connect() as conexion:
        resultado = conexion.execute(text("SELECT 1"))
        print("Conexión exitosa con MySQL")
        print("Resultado de la prueba:", resultado.scalar())

    # Cerrar el motor de conexión
    motor.dispose()


if __name__ == "__main__":
    main()
