# Sistema de Gestión de Personal

Aplicación web desarrollada con Django para administrar empleados, cargos y departamentos.

## Requisitos

- Python 3.13 o superior

## Instalación

En Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Ejecución

```powershell
python manage.py migrate
python manage.py runserver
```

La aplicación estará disponible en `http://127.0.0.1:8000/`.

Para acceder a Django Admin, crea un administrador con:

```powershell
python manage.py createsuperuser
```

Para un entorno real, define la variable `DJANGO_SECRET_KEY` antes de ejecutar
la aplicación. No guardes claves, contraseñas ni tokens dentro del repositorio.
