# Imagen base
FROM python:3.10-slim

RUN apt-get update && apt-get install -y postgresql-client

# Establecer directorio de trabajo
WORKDIR /app

# Copiar dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Variables de entorno
ENV FLASK_ENV=development
ENV DATABASE_URI=postgresql://myuser:mypassword@db:5432/mydatabase

# Comando por defecto
CMD ["python", "run.py"]
