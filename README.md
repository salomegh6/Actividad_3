# Actividad 3: Generación de datos con Python y MySQL

## 1. Descripción del proyecto

El proyecto consiste en generar e insertar 100.000 registros de personas ficticias en una base de datos MySQL mediante Python. Se utiliza Faker para generar los datos y SQLAlchemy para gestionar la conexión y las operaciones con la base de datos.

**Se utilizó**
- Python
- MySQL y PyMySQL
- SQLAlchemy
- Faker
- python-dotenv
- Git y GitHub
- DBeaver

## 2. Estructura del proyecto

El proyecto contiene los siguientes archivos:

- `main.py`: ejecuta la conexión a MySQL, la creación de la tabla y la inserción de los registros.
- `requirements.txt`: contiene las dependencias necesarias para ejecutar el programa.
- `README.md`: documenta el proyecto y sus instrucciones de uso.
- `.gitignore`: excluye archivos y carpetas que no deben publicarse.
- `.env.example`: proporciona una plantilla para configurar la conexión a MySQL.

El archivo `.gitignore` excluye `__pycache__/`, `.venv/`, `venv/` y `.env`. Esto evita publicar archivos de caché, entornos virtuales y credenciales privadas. El archivo `.env` se configura localmente, mientras que `.env.example` se publica con valores de ejemplo.

## 3. Instalación, configuración y ejecución

### Requisitos previos
- Tener Python instalado.
- Tener MySQL en funcionamiento.
- Tener creada la base de datos `Actividad_3`.

### Instalación de dependencias

Abrir una terminal en la carpeta del proyecto y ejecutar:

```bash
py -m pip install -r requirements.txt
```

Este comando instala las bibliotecas necesarias, especificadas en `requirements.txt`.

### Configuración de la conexión

Crear un archivo `.env` a partir de `.env.example` y configurar los datos de conexión a MySQL: host, puerto, usuario, contraseña y nombre de la base de datos.

El archivo `.env` contiene las credenciales reales y no debe publicarse en GitHub.

### Ejecución del programa

Desde la terminal, ubicada en la carpeta del proyecto, ejecutar:

```bash
py main.py
```

El programa establece la conexión con MySQL, crea la tabla `personas_salome` si no existe y genera los registros ficticios con Faker. Los datos se insertan en lotes de 1.000 registros.

## 4. Resultado final y verificación

Se generaron y almacenaron **100.000 registros ficticios** en la tabla `personas_salome`, dentro de la base de datos `Actividad_3`.

Para verificar el resultado desde DBeaver, ejecutar la siguiente consulta:

```sql
SELECT COUNT(*) FROM personas_salome;
```

El resultado esperado es `100000`.

Este proyecto permite practicar la conexión entre Python y MySQL, la generación automatizada de datos y el control de versiones mediante Git y GitHub.
