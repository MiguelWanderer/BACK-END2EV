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

## Funcionalidades

- Registro, inicio y cierre de sesión.
- Home principal con acceso a Administración de Personal.
- Gestión de empleados mediante interfaz propia.
- Administración de cargos, departamentos y empleados mediante Django Admin.
- Vista de listado, creación, detalle, edición y eliminación de empleados.
- Confirmación antes de eliminar un empleado.
- Protección del módulo para usuarios autenticados.

## Modelos y relaciones

El módulo `personal` contiene tres modelos:

- `Departamento`: almacena el nombre y la descripción de un área de la empresa.
- `Cargo`: almacena el nombre y la descripción de un cargo.
- `Empleado`: almacena los datos del trabajador y se relaciona con un cargo y un departamento.

`Empleado` utiliza dos claves foráneas:

```text
Empleado.cargo -> Cargo
Empleado.departamento -> Departamento
```

Esto representa una relación de muchos empleados para un cargo y muchos empleados
para un departamento. Se utiliza `on_delete=models.PROTECT` para impedir que se
elimine un cargo o departamento que todavía tenga empleados asociados.

## Uso de Django ORM

Las vistas consultan y modifican la base de datos mediante Django ORM. Algunos
ejemplos utilizados en el proyecto son:

```python
Empleado.objects.count()
Empleado.objects.select_related('cargo', 'departamento')
get_object_or_404(Empleado, pk=pk)
form.save()
empleado.delete()
```

El formulario `EmpleadoForm` es un `ModelForm`, por lo que los campos `cargo` y
`departamento` se cargan como opciones desde los registros existentes en la base de datos. No se utiliza SQL escrito manualmente.

## Autenticación y sesiones

Las vistas del módulo de personal están protegidas con `@login_required`. Un
usuario no autenticado es redirigido a `/accounts/login/`. Después de iniciar
sesión puede acceder a `/home/` y `/personal/`.

El registro utiliza `UserCreationForm` de Django. El inicio y cierre de sesión
utilizan las vistas integradas de autenticación, junto con el middleware de
sesiones y autenticación incluido en Django.

## Uso de Inteligencia Artificial

La Inteligencia Artificial se utilizó como herramienta de apoyo para:

- Proponer formularios, vistas CRUD y templates Django.
- Revisar errores de configuración y rutas.
- Sugerir mejoras de accesibilidad, estilos.
- Crear y revisar pruebas automáticas del flujo CRUD.

El código fue revisado, adaptado y validado ejecutando `manage.py check` y las
pruebas automatizadas del proyecto.
