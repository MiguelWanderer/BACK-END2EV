from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EmpleadoForm
from .models import Cargo, Departamento, Empleado


def home(request):
	return render(request, 'personal/home_principal.html')


def register(request):
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('login')
	return render(request, 'registration/register.html', {'form': form})


@login_required
def personal_home(request):
	context = {
		'total_empleados': Empleado.objects.count(),
		'total_cargos': Cargo.objects.count(),
		'total_departamentos': Departamento.objects.count(),
	}
	return render(request, 'personal/home.html', context)


@login_required
def empleado_list(request):
	empleados = Empleado.objects.select_related('cargo', 'departamento')
	return render(request, 'personal/empleado_list.html', {'empleados': empleados})


@login_required
def empleado_create(request):
	form = EmpleadoForm(request.POST or None)
	if form.is_valid():
		empleado = form.save()
		return redirect('personal:empleado_detail', pk=empleado.pk)
	return render(request, 'personal/empleado_form.html', {'form': form, 'titulo': 'Registrar empleado'})


@login_required
def empleado_detail(request, pk):
	empleado = get_object_or_404(
		Empleado.objects.select_related('cargo', 'departamento'),
		pk=pk,
	)
	return render(request, 'personal/empleado_detail.html', {'empleado': empleado})


@login_required
def empleado_update(request, pk):
	empleado = get_object_or_404(Empleado, pk=pk)
	form = EmpleadoForm(request.POST or None, instance=empleado)
	if form.is_valid():
		form.save()
		return redirect('personal:empleado_detail', pk=empleado.pk)
	return render(request, 'personal/empleado_form.html', {'form': form, 'titulo': 'Editar empleado'})


@login_required
def empleado_delete(request, pk):
	empleado = get_object_or_404(Empleado, pk=pk)
	if request.method == 'POST':
		empleado.delete()
		return redirect('personal:empleado_list')
	return render(request, 'personal/empleado_confirm_delete.html', {'empleado': empleado})
