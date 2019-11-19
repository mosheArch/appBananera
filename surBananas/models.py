from django.db import models
from .validators import name_capacitacion_validation
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
    choice_fase ={('', 'Areas'),('Area 1','Area 1'),('Area 2','Area 2'),('Area 3','Area 3'),('Area 4','Area 4'),('Area 5','Area 5'),('Unidad de Empaque','Unidad de Empaque'),('Unidad de Producción','Unidad de Producción')}
    choice_puesto= (('', 'Labor'),
                   ('1.- Unidad de Empaque', (
                       ('Recepción de Frutas', 'Recepción de Frutas'),
                       ('Desflore', 'Desflore'),
                       ('Lavador de Fomi', 'Lavador de Fomi'),
                       ('Armador de Carga', 'Armador de Carga'),
                       ('Evaluador de Fruta', 'Evaluador de Fruta'),
                       ('Clasificación', 'Clasificación'),
                       ('Selección', 'Selección'),
                       ('Selladoras', 'Selladoras'),
                       ('Pasador de Frutas', 'Pasador de Frutas'),
                       ('Empacador', 'Empacador'),
                       ('Repesado de Cajas Empacadas.', 'Repesado de Cajas Empacadas.'),
                       ('Desmane', 'Desmane'),
                       ('Estibador', 'Estibador'),
                       ('Pegador de Carton', 'Pegador de Carton'),
                       ('Preparación de Mezcla PosCosecha', 'Preparación de Mezcla PosCosecha'),
                       ('Limpieza', 'Limpieza'),
                       ('Dedo Suelto', 'Dedo Suelto'),
                       ('Bodega de Cartón', 'Bodega de Cartón'),
                       ('Evaluador de Cajas', 'Evaluador de Cajas'),
                       ('Jefe de Empaque', 'Jefe de Empaque'),

                   )),
                   ('2.- Unidad Producción', (
                       ('Deshije', 'Deshije'),
                       ('Aplicadores de Herbicidas', 'Aplicadores de Herbicidas'),
                       ('Desflore Manual', 'Desflore Manual'),
                       ('Cajeteo', 'Cajeteo'),
                       ('Saneo', 'Saneo'),
                       ('Paleo', 'Paleo'),
                       ('Fertilización', 'Fertilización'),
                       ('Riego y Bombeo', 'Riego y Bombeo'),
                       ('Chapeo de Rondas', 'Chapeo de Rondas'),
                       ('Picador de Matas', 'Picador de Matas'),
                       ('Desvio de Hijos y Rearme', 'Desvio de Hijos y Rearme'),
                       ('Técnico de Producción', 'Técnico de Producción'),
                       ('Jefe de Área', 'Jefe de Área'),
                       ('Cosecha', 'Cosecha'),
                       ('Embolse y Amarre.', 'Embolse y Amarre.'),
                       ('Fitosanitarios', 'Fitosanitarios'),
                       ('Seguridad', 'Seguridad'),
                       ('Responsable de Bodegas y Almacén', 'Responsable de Bodegas y Almacén'),
                       ('Taller y Mantenimiento.', 'Taller y Mantenimiento'),
                   )),

                   )
    fase = models.CharField(choices=choice_fase, default='', max_length=20, blank=True, null=True)
    puesto = models.CharField(choices=choice_puesto,max_length=20, blank=True, null=True, default='')
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
    choice_nacionalidad ={('', 'Nacionaidad'),('Mexicana','Mexicana'),('Extranjero','Extranjero')}
    choice_areas ='Areas'
    """choice_area =(('','Área'),
        ('Empaque',(
            ('Estiba','Estiba'),
            ('Empaque','Empaque'),
            ('Fumigación','Fumigación'),
            ('Selección', 'Selección'),
            ('Clasificación','Clasificación'),
            ('Desmane', 'Desmane'),
        )),
        ('Producción', (
            ('Embolse', 'Embolse'),
            ('Cosecha', 'Cosecha'),
            ('Fumigación', 'Fumigación'),
            ('Siembra', 'Siembra'),
        )),

    )"""
    codigoEmpleado = models.IntegerField(unique=True, primary_key=True)
    nombres = models.CharField(max_length=20, blank=True, null=True)
    apellidoPaterno = models.CharField(max_length=20, blank=True, null=True)
    apellidoMaterno = models.CharField(max_length=20, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    fechaNacimiento = models.DateField(auto_now=False, blank=True, null=True)
    numeroSeguroSocial = models.IntegerField(blank=True, null=True)
    curp = models.CharField(max_length=20, blank=True, null=True)
    rfc = models.CharField(max_length=20, blank=True, null=True)
    estadoCivil = models.CharField(max_length=20, blank=True, null=True)
    nacionalidad = models.CharField(choices=choice_nacionalidad, default='', max_length=20, blank=False)
    #area = models.CharField(choices=choice_area, default='', max_length=30, blank=False)
    #labor = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    celular = models.IntegerField(blank=True, null=True)
    correoElectronico = models.EmailField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    ciudad = models.CharField(max_length=200, blank=True, null=True)
    colonia = models.CharField(max_length=200, blank=True, null=True)
    codigoPostal = models.IntegerField(blank=True, null=True)
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



    








