from django.shortcuts import render, redirect, get_object_or_404
from empleados_app.forms import EmpleadoForm, CargaFamiliarForm, ContactoEmergenciaForm
from empleados_app.models import Empleado, CargaFamiliar

# Create your views here.

def listadoEmpleados(request):
    empleado = Empleado.objects.all()
    data = {'empleados': empleado }
    return render(request, 'listado_empleados.html', data)

def listarCargas(request, IN_id):
    empleado = get_object_or_404(Empleado, rut=IN_id)
    cargas = empleado.cargas_familiares.all()
    data = {'cargas': cargas, 'empleado': empleado}
    return render(request, 'listado_cargas.html', data)

def listarContactos(request, IN_id):
    empleado = get_object_or_404(Empleado, rut=IN_id)
    contactos = empleado.contactos.all()
    data = {'contactos': contactos, 'empleado': empleado}
    return render(request, 'listado_contactos.html', data)


def agregarEmpleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listado_empleados')
    else:
        form = EmpleadoForm()

    data = {'form_empleado': form}
    return render(request, 'formulario_empleado.html', data)

def agregar_cargas(request, empleado_rut):
    empleado = get_object_or_404(Empleado, rut=empleado_rut)

    if request.method == 'POST':
        form_carga = CargaFamiliarForm(request.POST)
        if form_carga.is_valid():
            carga_familiar = form_carga.save(commit=False)
            carga_familiar.empleado = empleado
            carga_familiar.save()
            return redirect('listar_cargas', IN_id=empleado.rut)
    else:
        form_carga = CargaFamiliarForm(initial={'empleado': empleado.rut})

    return render(request, 'formulario_cargas.html', {'empleado': empleado, 'form_carga': form_carga})


def agregar_contactos(request, empleado_rut):
    empleado = get_object_or_404(Empleado, rut=empleado_rut)

    if request.method == 'POST':
        form_contacto = ContactoEmergenciaForm(request.POST)
        if form_contacto.is_valid():
            contacto_emergencia = form_contacto.save(commit=False)
            contacto_emergencia.empleado = empleado
            contacto_emergencia.save()
            return redirect('listar_contactos', IN_id=empleado.rut)
    else:
        form_contacto = ContactoEmergenciaForm(initial={'empleado': empleado.rut})

    return render(request, 'formulario_contactos.html', {'empleado': empleado, 'form_contacto': form_contacto})









