# Proyecto Ingenieria de Software - Grupo 1 

## Setup
Primero deben crear un ambiente virutal  con

```python -m venv venv```

e instalar las dependencias con

```pip install -r requirements.txt```

Luego para mantener el codigo limpio se instalo `pre-commit` el cual deberas 
instalar con el siguiente comando dentro del ambiente virtual

```pre-commit install --hook-type pre-commit --hook-type pre-push```

Esto hara que cada vez que haga un commit se corra `black`, `isort` y `flake8` y
cada vez que se haga push se vea si falto hacer migraciones o falla algun test

