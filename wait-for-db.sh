#!/bin/bash
# Esperar hasta que PostgreSQL esté listo
until pg_isready -h db -p 5432 -U myuser; do
  echo "⏳ Esperando a que la base de datos esté lista..."
  sleep 2
done

# Ejecutar la app
python manage.py && python run.py
