# Utilizar una versión de Python
FROM python:latest

# Crear directorio de trabajo
WORKDIR /app

# Copiar los archivos requeridos a la imagen (app.py, templates, static)
COPY app.py /app/
COPY templates /app/templates
COPY static /app/static
# Simplificacion de la copia de archivos
#COPY . /app/

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Exponer el puerto que Flask utiliza (el mismo que has configurado en tu app.py)
EXPOSE 8080

# Establecer la variable de entorno FLASK_APP para que Flask pueda encontrar la aplicación
ENV FLASK_APP=app.py
# Establecer el entorno de Flask como desarrollo (puedes cambiarlo a production si es necesario)
ENV FLASK_ENV=development

# Ejecutar la aplicación Flask
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8080"]