# Proyecto Ingenieria de Software - Grupo 1 

## Setup
#### \*\*Instrucciones para sistemas unix-based
Primero deben crear un ambiente virutal  con

```bash
python -m venv venv
```

y luego se debe activar el ambiente con

```bash
source venv/bin/activate
```

e instalar las dependencias con

```bash
pip install -r requirements.txt
```

Luego para mantener el codigo limpio se instalo `pre-commit` el cual deberas 
instalar con el siguiente comando dentro del ambiente virtual

```bash
pre-commit install --hook-type pre-commit --hook-type pre-push
```

Esto hara que cada vez que haga un commit se corra `black`, `isort` y `flake8` y
cada vez que se haga push se vea si falto hacer migraciones o falla algun test

## Traducciones
Para hacer las traducciones existe `translations.sh`, para usarlo se debe ejecutar

```bash
./translations.sh <nombre de la app que se quiere traducir>
```

luego para compilar las traducciones se deber correr

```bash
./translations.sh -c <nombre de la app que se quiere traducir>
```

## Reset and populate db
Para resetear la base de datos se puede correr

```bash
./reset.sh
```

Para rellenar la base de datos con datos falsos se puede correr

```bash
./reset.sh -p
```

el cual borrara la base de datos actual y rellenara la base de datos con datos falsos.
