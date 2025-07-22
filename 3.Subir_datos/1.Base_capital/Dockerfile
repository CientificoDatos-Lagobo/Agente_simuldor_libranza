FROM python:3.13-slim

# Instala git para que gitpython funcione
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Directorio de trabajo (donde está el script)
WORKDIR /app/3.Subir_datos/1.Base_capital

# Copia requirements si tienes (opcional)
COPY requirements.txt .

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código (opcional si usas volumen)
# COPY . .

# CMD por defecto (puedes cambiarlo o sobrescribir con docker-compose)
CMD ["python", "app/Codigo.py"]
