from django.contrib import admin

from .models import Cargo, Departamento, Empleado


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'descripcion')
	search_fields = ('nombre', 'descripcion')
	ordering = ('nombre',)


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'descripcion')
	search_fields = ('nombre', 'descripcion')
	ordering = ('nombre',)


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
	list_display = (
		'rut',
		'nombre',
		'apellido',
		'cargo',
		'departamento',
		'estado',
	)
	search_fields = ('rut', 'nombre', 'apellido', 'correo')
	list_filter = ('cargo', 'departamento', 'estado')
	ordering = ('apellido', 'nombre')
