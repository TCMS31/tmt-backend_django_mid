#!/bin/bash

echo "Setting up venv..."
set -e
VENV_DIR=".venv"
python3 -m venv "$VENV_DIR"
source "$VENV_DIR/bin/activate"

echo "Installing requirements..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Migrating..."
./manage.py migrate --settings=config.settings.local

echo "Adding data to database..."
echo "from database import *" | python manage.py shell
