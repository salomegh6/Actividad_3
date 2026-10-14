# Actividad 3

## 1. Descripción
El proyecto consiste en generar e insertar 100.000 registros de personas ficticias en una base de datos MySQL mediante Python. Se utiliza Faker para generar los datos y SQLAlchemy para gestionar la conexión y las operaciones con la base de datos.

**Tecnologías utilizadas:**
- Python
- MySQL y PyMySQL
- SQLAlchemy
- Faker
- python-dotenv
- Git y GitHub
- DBeaver

## 2. Estructura
El proyecto contiene los siguientes archivos:
- `main.py`: ejecuta el proceso de conexión, creación de la tabla e inserción de datos.
- `requirements.txt`: especifica las dependencias necesarias.
- `.env.example`: proporciona una plantilla para configurar la conexión a MySQL.
- `.gitignore`: excluye `__pycache__/`, `.venv/`, `venv/` y `.env`.

El archivo `.env` contiene las credenciales reales y se mantiene local para evitar que se publiquen en GitHub. En cambio, `.env.example` se incluye en el repositorio con valores de ejemplo.

## 3. Funcionamiento
El programa establece la conexión con MySQL, crea la tabla `personas_salome` si no existe y genera registros con nombres, fechas de nacimiento, correos electrónicos, teléfonos, ciudades, direcciones, estados civiles y ocupaciones. Los datos se insertan en lotes de 1.000 registros.

Para ejecutar el proyecto, se instalan las dependencias con `py -m pip install -r requirements.txt`, se configura el archivo `.env` y se ejecuta `py main.py`.

## 4. Resultado final
Se generaron y almacenaron **100.000 registros ficticios** en la tabla `personas_salome` de la base de datos `actividad_3`. El resultado se verificó mediante DBeaver con la siguiente consulta:

```sql
SELECT COUNT(*) FROM personas_salome;
```

El proyecto permite practicar la conexión entre Python y MySQL, la generación automatizada de datos y el control de versiones mediante Git y GitHub.

