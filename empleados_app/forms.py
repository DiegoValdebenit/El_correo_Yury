from django import forms
from empleados_app.models import Empleado, CargaFamiliar, ContactoEmergencia

class EmpleadoForm(forms.ModelForm):
    SEXO = [('femenino','Femenino'), ('masculino', 'Masculino')]
    DEPARTAMENTO = [('departamento a','Departamento A'), ('departamento b', 'Departamento B'), ('departamento c', 'Departamento C')]
    AREA = [('area 1','Área 1'), ('area 2', 'Área 2'), ('area 3', 'Área 3')]
    CARGO = [('jefe de rrhh','Jefe de RRHH'), ('empleado de rrhh', 'Empleado de RRHH'), ('empleado de la empresa', 'Empleado de la Empresa')]

    class Meta:
        model = Empleado
        fields = '__all__'


    rut = forms.CharField()
    nombres = forms.CharField()
    apellidos = forms.CharField()
    email = forms.CharField()
    telefono = forms.CharField()
    direccion = forms.CharField()
    sexo = forms.ChoiceField(choices=SEXO, widget=forms.RadioSelect)
    fechaIngreso=forms.DateField()
    departamento = forms.CharField(widget=forms.Select(choices=DEPARTAMENTO))
    area = forms.CharField(widget=forms.Select(choices=AREA))
    cargo = forms.CharField(widget=forms.Select(choices=CARGO))


    def clean_nombres(self):
        input_nombres = self.cleaned_data['nombres']
        if len(input_nombres) > 80:
            raise forms.ValidationError("El largo máximo del nombre son 80 caracteres")
        return input_nombres

    def clean_email(self):
        input_email = self.cleaned_data['email']
        if not "@" in input_email:
            raise forms.ValidationError("Correo Electrónico incorrecto")
        return input_email



    fechaIngreso.widget.attrs['class'] = 'form-control'

class CargaFamiliarForm(forms.ModelForm):
    SEXO = [('femenino','Femenino'), ('masculino', 'Masculino')]

    class Meta:
        model = CargaFamiliar
        fields = '__all__'

    def __str__(self):
        return self.rut
    
    sexo = forms.ChoiceField(choices=SEXO, widget=forms.RadioSelect)


class ContactoEmergenciaForm(forms.ModelForm):
    class Meta:
        model = ContactoEmergencia
        fields = '__all__'
    
    def __str__(self):
        return self.rut
    

