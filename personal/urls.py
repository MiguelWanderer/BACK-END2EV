from django.urls import path

from . import views

app_name = 'personal'

urlpatterns = [
    path('registro/', views.register, name='register'),
    path('home/', views.home, name='home_principal'),
    path('', views.personal_home, name='home'),
    path('empleados/', views.empleado_list, name='empleado_list'),
    path('empleados/nuevo/', views.empleado_create, name='empleado_create'),
    path('empleados/<int:pk>/', views.empleado_detail, name='empleado_detail'),
    path('empleados/<int:pk>/editar/', views.empleado_update, name='empleado_update'),
    path('empleados/<int:pk>/eliminar/', views.empleado_delete, name='empleado_delete'),
]