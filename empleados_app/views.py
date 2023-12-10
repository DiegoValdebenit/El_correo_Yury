from django.shortcuts import render, redirect, get_object_or_404
from empleados_app.forms import EmpleadoForm, CargaFamiliarForm, ContactoEmergenciaForm
from empleados_app.models import Empleado, CargaFamiliar, ContactoEmergencia
from django.urls import reverse


# Create your views here.

def listadoEmpleados(request):
    # Obtener los parámetros de filtro de la url
    sexo = request.GET.get('sexo', None)
    cargo = request.GET.get('cargo', None)
    area = request.GET.get('area', None)
    departamento = request.GET.get('departamento', None)

    print(f'Sexo: {sexo}, Cargo: {cargo}, Área: {area}, Departamento: {departamento}')

    # Filtrar empleados según sexo, cargo, area o departamento
    empleados = Empleado.objects.all()

    if sexo:
        empleados = empleados.filter(sexo=sexo)
    if cargo:
        empleados = empleados.filter(cargo=cargo)
    if area:
        empleados = empleados.filter(area=area)
    if departamento:
        empleados = empleados.filter(departamento=departamento)

    data = {'empleados': empleados}
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


def eliminarEmpleado(request, IN_id):
    empleado = Empleado.objects.get(rut = IN_id)
    empleado.delete()
    return redirect('/listado_empleados')


def modificarDatos_personales(request, IN_id):
    empleado = get_object_or_404(Empleado, rut=IN_id)
    form = EmpleadoForm(instance=empleado)

    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('listadoEmpleados')

    data = {'form_empleado': form}
    return render(request, 'formulario_empleado.html', data)

def modificarCargas(request, empleado_rut, carga_id):
    empleado = get_object_or_404(Empleado, rut=empleado_rut)
    carga = get_object_or_404(CargaFamiliar, id=carga_id)

    if request.method == 'POST':
        form_carga = CargaFamiliarForm(request.POST, instance=carga)
        if form_carga.is_valid():
            form_carga.save()
            return redirect('listar_cargas', IN_id=empleado_rut)

    else:
        form_carga = CargaFamiliarForm(instance=carga)

    url_modificar_cargas = reverse('modificar_cargas', args=[empleado_rut, carga_id])
    return render(request, 'formulario_cargas.html', {'empleado': empleado, 'form_carga': form_carga, 'url_modificar_cargas': url_modificar_cargas})


def eliminarCarga(request, empleado_rut, carga_id):
    carga = get_object_or_404(CargaFamiliar, id=carga_id)
    if request.method == 'POST':
        carga.delete()
        return redirect('listar_cargas', IN_id=empleado_rut)

def modificarContactos(request, empleado_rut, contacto_id):
    empleado = get_object_or_404(Empleado, rut=empleado_rut)
    contacto = get_object_or_404(ContactoEmergencia, id=contacto_id)

    if request.method == 'POST':
        form_contacto = ContactoEmergenciaForm(request.POST, instance=contacto)
        if form_contacto.is_valid():
            form_contacto.save()
            return redirect('listar_contactos', IN_id=empleado_rut)

    else:
        form_contacto = ContactoEmergenciaForm(instance=contacto)

    url_modificar_contactos = reverse('modificar_contactos', args=[empleado_rut, contacto_id])
    return render(request, 'formulario_contactos.html', {'empleado': empleado, 'form_contacto': form_contacto, 'url_modificar_contactos': url_modificar_contactos})


def eliminarContacto(request, empleado_rut, contacto_id):
    contacto = get_object_or_404(ContactoEmergencia, id=contacto_id)
    if request.method == 'POST':
        contacto.delete()
        return redirect('listar_contactos', IN_id=empleado_rut)


