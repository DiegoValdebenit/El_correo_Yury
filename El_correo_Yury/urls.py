"""
URL configuration for El_correo_Yury project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from empleados_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listado_empleados/', views.listadoEmpleados, name='listadoEmpleados'),
    path('formulario_empleado/', views.agregarEmpleado),
    path('listado_cargas/<str:IN_id>/', views.listarCargas, name='listar_cargas'),
    path('listado_contactos/<str:IN_id>/', views.listarContactos, name='listar_contactos'),
    path('formulario_cargas/<str:empleado_rut>/', views.agregar_cargas, name='formulario_cargas'),
    path('formulario_contactos/<str:empleado_rut>/', views.agregar_contactos, name='formulario_contactos'),
    path('eliminar/<str:IN_id>/', views.eliminarEmpleado, name='eliminar_empleado'),
    path('actualizar/<str:IN_id>', views.modificarDatos_personales),

]
