from django.shortcuts import render, redirect
from empleados_app.forms import FormEmpleados, CargaFamiliarForm, ContactoEmergenciaForm

# Create your views here.

def agregarEmpleado(request):
    if request.method == 'POST':
        form = FormEmpleados(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/formulario_empleado')
    else:
        form = FormEmpleados()

    data = {'form_empleado': form}
    return render(request, 'formulario_empleado.html', data)


def agregarCarga(request):
    if request.method == 'POST':
        form = CargaFamiliarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/reservas')
    else:
        form = CargaFamiliarForm()

    data = {'form_carga_familiar': form}
    return render(request, 'formulario_contactos_cargas.html', data)

def agregarContacto(request):
    if request.method == 'POST':
        form = ContactoEmergenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/reservas')
    else:
        form = ContactoEmergenciaForm()

    data = {'form_contacto_emergencia': form}
    return render(request, 'formulario_contactos_cargas.html', data)
