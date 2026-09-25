from django import forms

from .models import Empleado


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = [
            'rut',
            'nombre',
            'apellido',
            'correo',
            'telefono',
            'fecha_ingreso',
            'cargo',
            'departamento',
            'estado',
        ]
        widgets = {
            'fecha_ingreso': forms.DateInput(attrs={'type': 'date'}),
        }