from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView,View
from django.views import generic
from .form import EmpleadosForm
from .formProgramas import ProgramasCapacitacion
from .AreasForm import AreasForm
from .AnualForm import Anual
from .BuscarEmpleadoForm import IncidenciasForm

from .CapacitacionForm import CapacitacionForm, DateForm
from .models import empleados, programasCapacitacion, areas, capacitacion, planAnual, incidencias
from django.urls import reverse_lazy
from pyexpat import model
from django.db.models.query import QuerySet
from telnetlib import STATUS
from django.http import HttpResponse
from django.views.generic import View
from django.conf import settings
from fpdf import FPDF
from datetime import datetime
from .fecha import *



parrafo = ''
a =''
b=''
c=''

def Dashboard(request):
    empleado= empleados.objects.filter(status=True)
    area = areas.objects.filter(status=True)
    programa = programasCapacitacion.objects.filter(status=True)
    capacitar = capacitacion.objects.filter(status=True)
    capacitacionTerminada = capacitacion.objects.filter(status=False)
    dashboard = {'empleado': empleado, 'area': area, 'programa': programa, 'capacitar': capacitar, 'capacitacionTerminada': capacitacionTerminada}

    return render(request, 'index.html',dashboard)

class crearCapacitacion(CreateView):
    model= programasCapacitacion
    template_name = 'crearCapacitacion.html'
    form_class = ProgramasCapacitacion
    success_url =  reverse_lazy('listaCapacitaciones')

class ListaCapacitacion(ListView):
    model = programasCapacitacion
    template_name = 'capacitaciones.html'
    context_object_name = 'capacitaciones'
    queryset = programasCapacitacion.objects.filter(status=True)

class ActualizarCapacitaciones(UpdateView):
    model = programasCapacitacion
    template_name = 'crearCapacitacion.html'
    form_class = ProgramasCapacitacion
    success_url = reverse_lazy('listaCapacitaciones')

class EliminarCapacitaciones(DeleteView):
    model = programasCapacitacion
    template_name = 'capacitaciones_confirm_delete.html'

    def post(self,request, pk, *args, **kwargs):
        object = programasCapacitacion.objects.get(id = pk)
        object.status = False
        object.save()
        return redirect('listaCapacitaciones')

class CrearEmpleado(CreateView):
    model = empleados
    template_name = 'agregarEmpleado.html'
    form_class = EmpleadosForm
    success_url = reverse_lazy('lista')



class ListaEmpleado(ListView):
    model = empleados
    template_name = 'empleados.html'
    context_object_name = 'empleados'
    queryset = empleados.objects.filter(status=True)
   

class ActualizarEmpleado(UpdateView):
    model = empleados
    template_name = 'agregarEmpleado.html'
    form_class = EmpleadosForm
    success_url = reverse_lazy('lista')

class EliminarEmpleado(DeleteView):
    model = empleados
    template_name = 'empleados_confirm_delete.html'

    def post(self,request, pk, *args, **kwargs):
        object = empleados.objects.get(codigoEmpleado = pk)
        object.status = False
        object.save()
        return redirect('lista')

class CrearArea(CreateView):
    model= areas
    template_name = 'agregarArea.html'
    form_class = AreasForm
    success_url = reverse_lazy('listaAreas')

class ListaArea(ListView):
    model = areas
    template_name = 'areas.html'
    context_object_name = 'areas'
    queryset = areas.objects.filter(status=True)

class ActualizarAreas(UpdateView):
    model = areas
    template_name = 'agregarArea.html'
    form_class = AreasForm
    success_url = reverse_lazy('listaAreas')

class EliminarArea(DeleteView):
    model = areas
    template_name = 'area_confirm_delete.html'

    def post(self,request, pk, *args, **kwargs):
        object = areas.objects.get(id = pk)
        object.status = False
        object.save()
        return redirect('listaAreas')

'''Modelo para crar Capacitaciones'''
class AsignarCapacitacion(CreateView):
    model= capacitacion
    template_name = 'agregarCapacitacion.html'
    form_class = CapacitacionForm
    success_url = reverse_lazy('listaAsignacion')

class ListaAsignacion(ListView):
    model = capacitacion
    template_name = 'capacitacionEmpleado.html'
    context_object_name = 'listaCapacitacion'
    queryset = capacitacion.objects.filter(status=True)

class Terminadas(ListView):
    model = capacitacion
    template_name = 'capacitacionesterminadas.html'
    context_object_name = 'terminadas'
    queryset = capacitacion.objects.filter(status=False)

class ActualizarAsignacion(UpdateView):
    model = capacitacion
    template_name = 'agregarCapacitacion.html'
    form_class = CapacitacionForm
    success_url = reverse_lazy('listaAsignacion')

class EliminarAsignacion(DeleteView):
    model = capacitacion
    template_name = 'asignacion_confirm_delete.html'

    def post(self,request, pk, *args, **kwargs):
        object = capacitacion.objects.get(id = pk)
        object.status = False
        object.save()
        return redirect('listaAsignacion')

def Card(request, pk):

    capacitar = empleados.objects.get(codigoEmpleado=pk)

    card = {'card': capacitar}

    return render(request, 'card.html',card)



class CrearPlanAnual(CreateView):
    model = planAnual
    template_name='crearPlanAnual.html'
    form_class=Anual
    success_url = reverse_lazy('listarplan')
    

class planlist(ListView):
    model = planAnual
    template_name= 'plan_list.html'
    context_object_name =  'planlist'


class EliminarPlanList (DeleteView):
    model = planAnual
    template_name = 'planAnual_confirm_delete.html'
    success_url = reverse_lazy('listarplan')

class ActualizarPlanAnual(UpdateView):
    model = planAnual
    template_name='crearPlanAnual.html'
    form_class=Anual
    success_url = reverse_lazy('listarplan')


class BuscarEmpleadoIncidencia (CreateView):
   model = incidencias
   template_name='BuscarEmpleado.html'
   form_class = IncidenciasForm
   success_url='BuscarEmpleadoIncidencia'
   
class Gincidencia(ListView):
  
    def post(self, request, *args, **kwargs):
        buscar = request.POST['codigoEmpleado']
        faltaa = int (request.POST['falta'])
        codigoT = empleados.objects.get(codigoEmpleado=buscar)
        nombre_jefe = request.POST['jefe']
        name_emp = str(codigoT.nombres)
        app_emp = str(codigoT.apellidoPaterno)
        apm_emp = str(codigoT.apellidoMaterno)
        nombreEmpleado = name_emp+' '+app_emp+' '+apm_emp
        pdf = FPDF(format='letter')
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(8,85,'FECHA:'+ fecha_actual)
        pdf.set_xy(150,48)
        pdf.cell(10,10,'ACTA ADMINISTRATIVA')
        if faltaa==1:
             global a,b,c,parrafo
             a='Por medio del presente escrito se levanta la acta administrativa al C. ' +nombreEmpleado+ ' ya que  en el reglamento interno del centro de trabajo EJIDO MIGUEL ALEMAN, se plasman las sanciones pertinentes, a la falta o incumplimiento del mismo,'
             b= 'el motivo por el cual se levanta la presente acta es lo siguiente: inclumplimiento del reglamento interno de inocuidad, con fecha ' +fecha_actual+ ' del presente año sin ninguna justificacion o notificacion, quedando plasmada que esta es la primera acta administrativa'
             c= 'con la cual ha sido sancionada, si en el dado caso hubiera reincidencia se procedera con una segunda y suspension de sus labores de forma temporal o si es el caso finalizacion del acuerdo laboral.'
            
             parrafo = a+b+c
            
        elif faltaa==2:
            a= 'Por medio del presente escrito se levanta la acta administrativa al C.' +nombreEmpleado+ ' ya que  en el reglamento interno del centro de trabajo EJIDO MIGUEL ALEMAN, se plasman las sanciones pertinentes, a la falta o incumplimiento del mismo'
            b='el motivo por el cual se levanta la presente acta es lo siguiente: Por no asistir a sus labores del dia '+ fecha_actual+ ' del presente año sin ninguna justificacion o notificacion, quedando plasmada que esta es la primera acta administrativa'
            c= 'con la cual ha sido sancionada, si en el dado caso hubiera reincidencia se procedera con una segunda y suspension de sus labores de forma temporal o si es el caso finalizacion del acuerdo laboral.'
            
            parrafo = a+b+c
           

        elif faltaa==3:
            a= 'Por medio del presente escrito se levanta la acta administrativa al C. '+ nombreEmpleado +' ya que  en el reglamento interno del centro de trabajo EJIDO MIGUEL ALEMAN, se plasman las sanciones pertinentes, a la falta o incumplimiento del mismo,'
            b='el motivo por el cual se levanta la presente acta es lo siguiente: Por falta de respeto a un compañero laboral, quedando plasmada que esta es la primera acta administrativa'
            c= 'con la cual ha sido sancionada, si en el dado caso hubiera reincidencia se procedera con una segunda y suspension de sus labores de forma temporal o si es el caso finalizacion del acuerdo laboral.'
           
            parrafo = a+b+c
        
        elif faltaa==4:
            a= 'Por medio del presente escrito se levanta la acta administrativa al C. '+ nombreEmpleado +' ya que  en el reglamento interno del centro de trabajo EJIDO MIGUEL ALEMAN, se plasman las sanciones pertinentes, a la falta o incumplimiento del mismo,'
            b='el motivo por el cual se levanta la presente acta es lo siguiente: Por no usar o usar inadecuadamente EPP, quedando plasmada que esta es la primera acta administrativa'
            c= 'con la cual ha sido sancionada, si en el dado caso hubiera reincidencia se procedera con una segunda y suspension de sus labores de forma temporal o si es el caso finalizacion del acuerdo laboral.'
           
            parrafo = a+b+c

        elif faltaa==5:
            a= 'Por medio del presente escrito se levanta la acta administrativa  C. '+ nombreEmpleado +' ya que  en el reglamento interno del centro de trabajo EJIDO MIGUEL ALEMAN, se plasman las sanciones pertinentes, a la falta o incumplimiento del mismo,'
            b='el motivo por el cual se levanta la presente acta es lo siguiente: Por haberse presentado a laborar el dia de hoy ' +fecha_actual + ', bajo influencias de sustancias prohibidas/estupefacientes. Quedando plasmada que esta es la primera acta administrativa'
            c= 'con la cual ha sido sancionada, si en el dado caso hubiera reincidencia se procedera con una segunda y suspension de sus labores de forma temporal o si es el caso finalizacion del acuerdo laboral.'
           
            parrafo = a+b+c

        elif faltaa==6:
            a= 'Por medio del presente escrito se levanta la acta administrativa  C. '+ nombreEmpleado +' ya que  en el reglamento interno del centro de trabajo EJIDO MIGUEL ALEMAN, se plasman las sanciones pertinentes, a la falta o incumplimiento del mismo,'
            b='el motivo por el cual se levanta la presente acta es lo siguiente: Por presentar varios retardos constantes. Quedando plasmada que esta es la primera acta administrativa'
            c= 'con la cual ha sido sancionada, si en el dado caso hubiera reincidencia se procedera con una segunda y suspension de sus labores de forma temporal o si es el caso finalizacion del acuerdo laboral.'
           
            parrafo = a+b+c
                 
        
        
        pdf.set_xy(8,70)
        pdf.multi_cell(200, 10, parrafo, align="J")
        pdf.cell(200,80,'ATENTAMENTE',align="C")
        pdf.set_font('Times', 'U')
        pdf.set_xy(8,170)
        pdf.cell(10,80,nombre_jefe)
        pdf.set_font('Times')
        pdf.set_xy(8,170)
        pdf.cell(4,89,'NOMBRE Y FIRMA DEL JEFE DE AREA')
        pdf.set_font('Times', 'U')
        pdf.set_xy(130,207)
        pdf.cell(8,5,nombreEmpleado)
        pdf.set_font('Times')
        pdf.set_xy(147,212)
        pdf.cell(8,5,'PERSONA SANCIONADA')
        pdf.set_font('Times', 'U')
        pdf.set_xy(8,240)
        pdf.cell(10,10,'ING.ANGEL ENRIQUE GIRON DE LEON')
        pdf.set_xy(15,247)
        pdf.set_font('Times')
        pdf.cell(8,5,'GERENTE DE PRODUCCION')
        pdf.set_font('Times','U')
        pdf.set_xy(125,242)
        pdf.cell(8,5,'PRESENTANTE DE LOS TRABAJADORES')
        pdf.set_xy(125,247)
        pdf.set_font('Times')
        pdf.cell(8,5,'COMISION DE SEGURIDAD E HIGIENE')

        
        response = HttpResponse(pdf.output(dest='S').encode('latin-1'))
        response['Content-Type'] = 'application/pdf'
        response['Content-Disposition'] = 'attachment;filename="documento.pdf"'
        return response



class PrintPlanAnual(ListView):
    model = planAnual
    template_name= 'acta.html'
    context_object_name =  'planlist'
