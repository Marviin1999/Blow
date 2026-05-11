#!/usr/bin/env bash
# salir si ocurre un error
set -o errexit

# Instalar dependencias
pip install -r requirements.txt

# Recolectar archivos estáticos (para que el panel de admin se vea bien)
python manage.py collectstatic --no-input

# Aplicar migraciones de la base de datos
python manage.py migrate