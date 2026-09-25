from datetime import date

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Cargo, Departamento, Empleado


class EmpleadoCrudTests(TestCase):
	def setUp(self):
		self.usuario = User.objects.create_user(
			username='usuario_prueba',
			password='ClaveSegura123!',
		)
		self.cargo = Cargo.objects.create(nombre='Analista')
		self.departamento = Departamento.objects.create(nombre='Informatica')
		self.empleado = Empleado.objects.create(
			rut='12.345.678-9',
			nombre='Ana',
			apellido='Perez',
			correo='ana@example.com',
			telefono='+56912345678',
			fecha_ingreso=date(2024, 3, 10),
			cargo=self.cargo,
			departamento=self.departamento,
		)

	def test_modulo_requiere_autenticacion(self):
		response = self.client.get(reverse('personal:empleado_list'))
		self.assertRedirects(
			response,
			f'{reverse("login")}?next={reverse("personal:empleado_list")}',
		)

	def test_usuario_autenticado_puede_ver_empleado(self):
		self.client.login(username='usuario_prueba', password='ClaveSegura123!')
		response = self.client.get(reverse('personal:empleado_detail', args=[self.empleado.pk]))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Ana Perez')

	def test_usuario_autenticado_puede_crear_empleado(self):
		self.client.login(username='usuario_prueba', password='ClaveSegura123!')
		response = self.client.post(
			reverse('personal:empleado_create'),
			{
				'rut': '98.765.432-1',
				'nombre': 'Luis',
				'apellido': 'Gonzalez',
				'correo': 'luis@example.com',
				'telefono': '+56987654321',
				'fecha_ingreso': '2025-01-15',
				'cargo': self.cargo.pk,
				'departamento': self.departamento.pk,
				'estado': Empleado.Estado.ACTIVO,
			},
		)
		self.assertRedirects(
			response,
			reverse('personal:empleado_detail', args=[Empleado.objects.latest('id').pk]),
		)
		self.assertTrue(Empleado.objects.filter(rut='98.765.432-1').exists())

	def test_usuario_autenticado_puede_eliminar_empleado(self):
		self.client.login(username='usuario_prueba', password='ClaveSegura123!')
		confirmation = self.client.get(
			reverse('personal:empleado_delete', args=[self.empleado.pk]),
		)
		self.assertEqual(confirmation.status_code, 200)
		self.assertContains(confirmation, '¿Está seguro de que desea eliminar')
		response = self.client.post(
			reverse('personal:empleado_delete', args=[self.empleado.pk]),
		)
		self.assertRedirects(response, reverse('personal:empleado_list'))
		self.assertFalse(Empleado.objects.filter(pk=self.empleado.pk).exists())
