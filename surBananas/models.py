from django.db import models


class programasCapacitacion(models.Model):
    temaCapacitacion = models.TextField(max_length=50, blank=True, null=True)
    descripcionCapacitacion = models.TextField(max_length=100, blank=True, null=True)
    tipoCapacitacion = models.TextField(max_length=50, blank=True, null=True)
    status = models.BooleanField('Estado', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        if self.temaCapacitacion == None:
            return "----------"
        return self.temaCapacitacion


class areas(models.Model):
    choice_riesgo ={('', 'Tipos de riesgo'),('Físico','Físico'),('Quimico','Quimico'), ('Físico y Quimico','Físico y Quimico')}
  
    puesto = models.CharField(max_length=100, blank=True, null=True)
    actividad = models.CharField(max_length=500, blank=True, null=True)
    tiposRiesgo = models.CharField(choices=choice_riesgo, default='', max_length=20, blank=True, null=True)
    regionAnatomica = models.CharField(max_length=200,blank=True, null=True)
    eppUtilizar = models.CharField(max_length=200,blank=True, null=True)
    status = models.BooleanField('Estado', default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        if self.puesto == None:
            return "----------"
        return self.puesto


class empleados(models.Model):
    choice_fase ={('', 'Areas'),('Area 1','Area 1'),('Area 2','Area 2'),('Area 3','Area 3'),('Area 4','Area 4'),('Area 5','Area 5'),('Unidad de Empaque','Unidad de Empaque'),('Unidad de Producción','Unidad de Producción'),('Nutricion','Nutricion'),('Riego','Riego'),('Moko','Moko'),('Sigatoka','Sigatoka'), ('Seguridad','Seguridad'),('Otros','Otros')}
    fase = models.CharField(choices=choice_fase, default='', max_length=20, blank=True, null=True)
    codigoEmpleado = models.CharField(max_length=100, unique=True, primary_key=True)
    nombres = models.CharField(max_length=30, blank=True, null=True)
    apellidoPaterno = models.CharField(max_length=30, blank=True, null=True)
    apellidoMaterno = models.CharField(max_length=30, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    fechaNacimiento = models.DateField(auto_now=False, blank=True, null=True)
    numeroSeguroSocial = models.CharField(max_length=100, blank=True, null=True)
    curp = models.CharField(max_length=20, blank=True, null=True)
    rfc = models.CharField(max_length=20, blank=True, null=True)
    estadoCivil = models.CharField(max_length=20, blank=True, null=True)
    nacionalidad = models.CharField(max_length=100,blank=True, null=False)
    telefono = models.IntegerField(max_length=20, blank=True, null=True)
    celular = models.IntegerField(max_length=20, blank=True, null=True)
    correoElectronico = models.EmailField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    ciudad = models.CharField(max_length=200, blank=True, null=True)
    colonia = models.CharField(max_length=200, blank=True, null=True)
    codigoPostal = models.IntegerField(max_length=20, blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    imagen = models.ImageField(upload_to="fotos/", blank=True, null=True)
    area = models.ForeignKey(areas, on_delete=models.CASCADE)
    
    status = models.BooleanField('¡Dar de baja!', default= True)    
    fechaEliminacion = models.DateField(auto_now=False, blank=True, null=True)
    motivoEliminacion = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        if self.nombres == None:
            return "----------"
        return self.nombres



class capacitacion(models.Model):
    nombreCapacitacion = models.CharField(max_length=200, blank=True, null=True)
    empleado = models.ForeignKey(empleados, on_delete=models.CASCADE)
    programas = models.ForeignKey(programasCapacitacion, on_delete=models.CASCADE)
    fechaCapacitacion = models.DateField(auto_now=False, blank=True, null=True)
    status = models.BooleanField('Estado', default=True)
    capacitacionTeminada = models.BooleanField('Capacitado', default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)



class planAnual (models.Model):
    objetivoG = models.CharField(max_length=500, blank=True, null=True)
    dirigido = models.CharField(max_length=500, blank=True, null=True)
    tema = models.CharField(max_length=500, blank=True, null=True)
    objetivoe = models.CharField(max_length=500, blank=True, null=True)
    contenido = models.CharField(max_length=500, blank=True, null=True)
    tecnicas = models.CharField(max_length=500, blank=True, null=True)
    dirigidoaquien = models.CharField(max_length=500, blank=True, null=True)
    duracion = models.CharField(max_length=500, blank=True, null=True)
    status = models.BooleanField('Estado', default=True)
    create_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class incidencias (models.Model):
    codigoEmpleado = models.ForeignKey(empleados,null=True, blank=True, on_delete=models.CASCADE)
    totalfaltas = models.IntegerField(blank=True, null=True)



    








