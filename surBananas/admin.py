from django.contrib import admin
from .models import empleados, programasCapacitacion, areas, capacitacion, planAnual

admin.site.register(empleados)
admin.site.register(programasCapacitacion)
admin.site.register(areas)
admin.site.register(capacitacion)
admin.site.register(planAnual)

