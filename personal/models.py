from django.db import models


class Departamento(models.Model):
	nombre = models.CharField(max_length=100, unique=True)
	descripcion = models.TextField(blank=True)

	class Meta:
		ordering = ['nombre']
		verbose_name = 'departamento'
		verbose_name_plural = 'departamentos'

	def __str__(self):
		return self.nombre


class Cargo(models.Model):
	nombre = models.CharField(max_length=100, unique=True)
	descripcion = models.TextField(blank=True)

	class Meta:
		ordering = ['nombre']
		verbose_name = 'cargo'
		verbose_name_plural = 'cargos'

	def __str__(self):
		return self.nombre


class Empleado(models.Model):
	class Estado(models.TextChoices):
		ACTIVO = 'ACTIVO', 'Activo'
		INACTIVO = 'INACTIVO', 'Inactivo'

	rut = models.CharField(max_length=12, unique=True)
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	correo = models.EmailField()
	telefono = models.CharField(max_length=30)
	fecha_ingreso = models.DateField()
	cargo = models.ForeignKey(
		Cargo,
		on_delete=models.PROTECT,
		related_name='empleados',
	)
	departamento = models.ForeignKey(
		Departamento,
		on_delete=models.PROTECT,
		related_name='empleados',
	)
	estado = models.CharField(
		max_length=8,
		choices=Estado.choices,
		default=Estado.ACTIVO,
	)

	class Meta:
		ordering = ['apellido', 'nombre']
		verbose_name = 'empleado'
		verbose_name_plural = 'empleados'

	def __str__(self):
		return f'{self.nombre} {self.apellido}'
