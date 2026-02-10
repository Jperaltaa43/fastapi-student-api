# FastAPI Student API

REST API desarrollada con FastAPI para la gestión de estudiantes, cursos y
sus inscripciones. Implementa validaciones, manejo de errores HTTP y relaciones
entre entidades usando SQLAlchemy.

---

## Tecnologías

- Python 3.10+
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite
- Uvicorn

---

## Estructura del proyecto

Arquitectura del proyecto

FASTAPI STUDENT API/

|  ├── app/

│ ├── main.py

│ ├── database.py

│ ├── crud.py

│ ├── models.py

│ ├── schemas.py

│ └── routers/

│       ├── students.py

│       ├── courses.py

│       └── enrollments.py

├── requirements.txt

└── README.md


## Ejecución local

1. Clonar el repositorio

```bash
git clone https://github.com/Jperaltaa43/fastapi-student-api.git
cd fastapi-student-api


1️⃣ Clonar el repositorio
git clone https://github.com/Jperaltaa43/fastapi-student-api.git
cd fastapi-student-api

2️⃣ Crear entorno virtual
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

3️⃣ Instalar dependencias
pip install -r requirements.txt

4️⃣ Ejecutar el servidor
uvicorn app.main:app --reload

Documentación (Swagger)

FastAPI genera documentación automática:

Swagger UI:
http://127.0.0.1:8000/docs

ReDoc:
http://127.0.0.1:8000/redoc

Endpoints principales:

Students:
Método	                          Endpoint	                  Descripción
POST	                           /students/                   Crear estudiante
GET	                           /students/                   Listar estudiantes
GET	                           /students/{id}               Obtener estudiante
PUT	                           /students/{id}               Actualizar estudiante
DELETE	                           /students/{id}               Eliminar estudiante

Courses:
Método	                           Endpoint	                  Descripción
POST	                           /courses/                        Crear curso
GET	                           /courses/                        Listar cursos
GET	                           /courses/{id}                    Obtener curso
DELETE	                           /courses/{id}                    Eliminar curso

Enrollments:
Método	                           Endpoint	                  Descripción
POST	                           /enrollments/                    Inscribir estudiante
GET	                           /enrollments/                    Listar inscripciones


Validaciones y manejo de errores

El sistema valida automáticamente:

Emails con formato correcto
Longitud mínima de nombres
IDs inexistentes (404)
Duplicados de inscripciones (409)
Referencias inválidas entre entidades

Ejemplo de error:
{
  "detail": "Student not found"
}


Casos de prueba recomendados

GET /students/999 → estudiante inexistente
POST /students/ con email inválido
Inscribir dos veces al mismo estudiante en un curso
Crear curso con título demasiado corto


Buenas prácticas aplicadas:

Separación clara de responsabilidades
Routers desacoplados de la lógica de negocio
Validaciones a nivel de esquema y base de datos
Código legible y mantenible
Listo para escalar a producción

Posibles mejoras futuras:


Autenticación JWT
Roles (admin / user)
Paginación y filtros
Migraciones con Alembic
Tests automáticos con Pytest
Dockerización

Autor
Jesús Iván Peralta
Estudiante de Ingeniería en Sistemas Computacionales

