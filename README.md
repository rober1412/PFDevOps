#  Reto Final DevOps - Entorno Local

Este proyecto es una API REST básica desarrollada con Flask y conectada a una base de datos PostgreSQL. Todo corre en contenedores Docker usando `docker-compose`.

---
<nbsp>
</nbsp>

##  Estructura del proyecto

```bash
reto_final_python/
├── app/
│   ├── __init__.py         # Inicializa la app Flask y registra rutas
│   ├── config.py           # Configuración por entorno
│   ├── models.py           # Modelo Data (ORM con SQLAlchemy)
│   └── routes.py           # Endpoints de la API
├── tests/
│   └── test_routes.py      # Tests unitarios con pytest
├── Dockerfile              # Imagen del servicio web
├── docker-compose.yml      # Orquestador de servicios
├── wait-for-db.sh          # Espera a que PostgreSQL esté lista
├── manage.py               # Crea tablas e inserta datos (si aplica)
├── requirements.txt        # Dependencias del proyecto
└── README.md               # Este documento
```

<nbsp>
</nbsp>

## Cómo levantar el entorno
#### Requisitos previos
- Docker instalado (descargar)
- Docker Compose (ya viene con Docker Desktop)

#### Pasos para ejecutar
```bash
git clone <URL_DEL_REPOSITORIO>
cd reto_final_python
docker-compose up --build
```
La app estará disponible en http://localhost:5000

<nbsp>
</nbsp>

## Endpoints disponibles
|Método|Endpoint|Descripción|
| ------------ | ------------ | ------------ |
| GET | /data  | Obtener todos los registros |
| POST | /data  | Crear un nuevo registro |
| DELETE | /data/< id > |  Eliminar un registro por ID |

<nbsp>
</nbsp>

## Ejemplos de uso con curl
```bash
curl -X POST http://localhost:5000/data \
     -H "Content-Type: application/json" \
     -d '{"name": "Ejemplo"}'
curl http://localhost:5000/data
curl -X DELETE http://localhost:5000/data/1
```
<nbsp>
</nbsp>

## Tests unitarios
El proyecto incluye una batería de tests desarrollados con **pytest**, que prueban:
- Inserción de datos (POST)
- Consulta de datos (GET)
- Eliminación de datos (DELETE)

Los tests usan una base de datos SQLite en memoria, completamente aislada del entorno real.

## Ejecutar los tests dentro del contenedor:
```bash
# Acceder al contenedor web
docker exec -it reto_final_python-web-1 bash

# Ejecutar tests
PYTHONPATH=. pytest
```

<nbsp>
</nbsp>

## Cobertura de código
La cobertura fue medida con **coverage.py** y alcanza un 96%.

|  Archivo |Cobertura|
| ------------ | ------------ |
| app/__init__.py  |  100% |
|  app/config.py |  100% |
|  app/models.py |  83% |
|  app/routes.py |  92% |
|  tests/test_routes.py |  100% |
|  **Total** |  **96%** |

### Comandos usados
```bash
coverage run -m pytest
coverage report
```

<nbsp>
</nbsp>

## Notas importantes
- El script manage.py se ejecuta al arrancar para crear las tablas.
- wait-for-db.sh asegura que la base de datos esté lista antes de iniciar Flask.
- No usar este entorno en producción tal como está.
