# https://hub.docker.com/_/python
# Dockerfile para el contener de python 3
FROM python:3

#Definimos nuestro directorio como directorio de trabajo
WORKDIR /app

#Copaimos archivo de dependencias necesarios
COPY requirements.txt .

#Actualizamos pip
RUN pip install --upgrade pip

#Instalamos dependencias
RUN pip install --no-cache-dir  -r requirements.txt

#Copiamos nuestros archivos
COPY /app ./

#Definimos nuestro servicio
ENV FLASK_APP=/app/controllers/app.py

RUN py.test