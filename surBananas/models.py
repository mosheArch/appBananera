from django.db import models

class programasCapacitacion(models.Model):
    temaCapacitacion = models.TextField(max_length=50, blank=True, null=True)
    descripcionCapacitacion = models.TextField(max_length=100, blank=True, null=True)
    tipoCapacitacion = models.TextField(max_length=50, blank=True, null=True)
    status = models.BooleanField('Estado', default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class empleados(models.Model):
    nombres = models.CharField(max_length=20, blank=True, null=True)
    apellidoPaterno = models.CharField(max_length=20, blank=True, null=True)
    apellidoMaterno = models.CharField(max_length=20, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    fechaNacimiento = models.DateField(auto_now=False, blank=True, null=True)
    numeroSeguroSocial = models.IntegerField(blank=True, null=True)
    curp = models.CharField(max_length=20, blank=True, null=True)
    rfc = models.CharField(max_length=20, blank=True, null=True)
    estadoCivil = models.CharField(max_length=20, blank=True, null=True)
    nacionalidad = models.CharField(max_length=20, blank=True, null=True)
    area = models.CharField(max_length=30, blank=True, null=True)
    labor = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    celular = models.IntegerField(blank=True, null=True)
    correoElectronico = models.EmailField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    ciudad = models.CharField(max_length=200, blank=True, null=True)
    colonia = models.CharField(max_length=200, blank=True, null=True)
    codigoPostal = models.IntegerField(blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    imagen = models.FileField(upload_to="fotos/", blank=True, null=True)
    status = models.BooleanField('Estado', default= True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class capacitacion(models.Model):
    empleado = models.ForeignKey(empleados, on_delete=models.CASCADE)
    programas = models.ForeignKey(programasCapacitacion, on_delete=models.CASCADE)
    fechaCapacitacion = models.DateField(auto_now=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

