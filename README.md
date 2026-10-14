
# Actividad 3

# 1. Descripción 
El proyecto consiste en generar e insertar 100.000 registros de personas ficticias en una base de datos MySQL mediante Python. Se utilizan Faker para generar los datos y SQLAlchemy para gestionar la conexión y las operaciones con la base de datos.

Se utilizó:
- Python
- MySQL 
- SQLAlchemy
- Faker
- Git y GitHub
- DBeaver

# 2. Estructura 
El proyecto contiene `main.py`, que ejecuta el proceso; `requirements.txt`, que especifica las dependencias; `.env.example`, que sirve como plantilla de configuración; y `.gitignore`, que excluye `__pycache__/`, `.venv/`, `venv/` y `.env`. Estos archivos se ignoran para evitar publicar archivos temporales, entornos virtuales y credenciales privadas. El archivo `.env` se configura localmente y no debe subirse al repositorio.

# 3. Funcionamiento
El programa establece la conexión con MySQL, crea la tabla `personas_salome` si no existe y genera registros con nombres, fechas de nacimiento, correos electrónicos, teléfonos, ciudades, direcciones, estados civiles y ocupaciones. Los datos se insertan en lotes de 1.000 registros. Para ejecutarlo, se instalan las dependencias con `py -m pip install -r requirements.txt` y se utiliza el comando `py main.py`.

# 4. Resultado final
Se logró generar y almacenar un total de **100.000 registros ficticios** en la tabla `personas_salome` de la base de datos `actividad_3`. El resultado se verificó mediante DBeaver con la consulta:

```sql
SELECT COUNT(*) FROM personas_salome;
```

El proyecto permite practicar la conexión entre Python y MySQL, la generación automatizada de datos y el control de versiones con Git y GitHub.
