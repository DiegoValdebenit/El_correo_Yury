from django.db import models


# Create your models here.

class Empleado(models.Model):
    rut = models.CharField(max_length=15, primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField(max_length= 70)
    telefono = models.CharField(max_length=30)
    direccion = models.CharField(max_length=70)
    sexo = models.CharField(max_length=10)
    fechaIngreso = models.DateField()
    departamento = models.CharField(max_length=15)
    area = models.CharField(max_length=15)
    cargo = models.CharField(max_length=25)

class CargaFamiliar(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    rut = models.CharField(max_length=15)
    parentesco = models.CharField(max_length=50)

class ContactoEmergencia(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    relacion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=30)



