#  Reto Final DevOps - Entorno Local 

Este proyecto es una API REST básica desarrollada con Flask y conectada a una base de datos PostgreSQL. Todo corre en contenedores Docker usando `docker-compose`.

---

##Estructura del proyecto

```bash
├── app/
│   ├── __init__.py       
│   ├── config.py          
│   ├── models.py        
│   └── routes.py      
├── Dockerfile          
├── docker-compose.yml     
├── manage.py             
├── wait-for-db.sh      
├── requirements.txt       
└── README.md            
```
---

## Cómo levantar el entorno

###  Requisitos previos

- Tener [Docker](https://www.docker.com/products/docker-desktop/) instalado
- Tener Docker Compose (ya viene con Docker Desktop)

###  Comandos para ejecutar

**1. **Clonar el repositorio:
```bash
git clone <URL_DEL_REPOSITORIO>
cd reto_final_python
```
**2. **Levantar los servicios:
```bash
docker-compose up --build
```
**3.** La aplicación estará disponible en:
```bash
http://localhost:5000
```

## Endpoints disponibles

| Método | Endpoint     | Descripción                   |
|--------|--------------|-------------------------------|
| GET    | `/data`      | Obtener todos los registros   |
| POST   | `/data`      | Crear un nuevo registro       |
| DELETE | `/data/<id>` | Eliminar un registro por ID   |

## Ejemplos de uso con curl
#### 1. Insertar dato (POST)
curl -X POST http://localhost:5000/data \
     -H "Content-Type: application/json" \
     -d '{"name": "Ejemplo"}'
#### 2. Obtener todos los datos (GET)
curl http://localhost:5000/data
#### 3. Eliminar un dato por ID (DELETE)
curl -X DELETE http://localhost:5000/data/1

## ¿Qué contiene este proyecto?
- Python 3.10
-  Flask
- SQLAlchemy
- PostgreSQL 14
- Docker
- Docker compose

## Notas importantes
- El script manage.py se ejecuta automáticamente para crear las tablas.
- wait-for-db.sh evita errores esperando a que la base de datos esté lista.









