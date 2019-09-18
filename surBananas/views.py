from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from .form import EmpleadosForm
from .formProgramas import ProgramasCapacitacion
from .models import empleados, programasCapacitacion
from django.urls import reverse_lazy



class Inicio(TemplateView):
    model = empleados
    form_class = EmpleadosForm
    template_name = 'index.html'

class Home(TemplateView):
    model = empleados
    form_class = EmpleadosForm
    template_name = 'index.html'


class crearCapacitacion(CreateView):
    model= programasCapacitacion
    template_name = 'crearCapacitacion.html'
    form_class = ProgramasCapacitacion
    success_url =  reverse_lazy('listaCapacitacion')

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
        object = empleados.objects.get(id = pk)
        object.status = False
        object.save()
        return redirect('lista')
