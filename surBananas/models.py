from django.db import models

class progrmasCapacitacion(models.Model):
    temaCapacitacion = models.TextField(max_length=50, blank=True, null=True)
    descripcionCapacitacion = models.TextField(max_length=100, blank=True, null=True)
    tipoCapacitacion = models.TextField(max_length=50, blank=True, null=True)
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
    programas = models.ManyToManyField(progrmasCapacitacion, through='capacitacion')


class capacitacion(models.Model):
    empleado = models.ForeignKey(empleados, on_delete=models.CASCADE)
    programas = models.ForeignKey(progrmasCapacitacion, on_delete=models.CASCADE)
    fechaCapacitacion = models.DateField(auto_now=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)


# class planCapacitacion(models.Model):
#     empleado = models.ForeignKey(empleados, on_delete=models.CASCADE)
#     temaCapacitacion = models.TextField(max_length=50, blank=True, null=True)
#     descripcionCapacitacion = models.TextField(max_length=100, blank=True, null=True)
#     fechaCapacitacion = models.DateField(auto_now=False, blank=True, null=True)
#
# class planSalud(models.Model):
#     empleado = models.ForeignKey(empleados, on_delete=models.CASCADE)
#     temaPlanSalud = models.TextField(max_length=100, blank=True, null=True)
#     descripcionTemaSalud = models.TextField(max_length=100, blank=True, null=True)
#     fechaPlanSalud = models.DateField(auto_now=False, blank=True, null=True)
#
# class planMantenimieto(models.Model):
#     empleado = models.ForeignKey(empleados, on_delete=models.CASCADE)
#     temaPlanMantenimiento = models.TextField(max_length=100, blank=True, null=True)
#     descripcionMantenimiento = models.TextField(max_length=100, blank=True, null=True)
#     fechaMantenimiento = models.DateField(auto_now=False, blank=True, null=True)
