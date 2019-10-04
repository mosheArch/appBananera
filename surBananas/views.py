from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from .form import EmpleadosForm
from .formProgramas import ProgramasCapacitacion
from .AreasForm import AreasForm
from .CapacitacionForm import CapacitacionForm
from .models import empleados, programasCapacitacion, areas, capacitacion
from django.urls import reverse_lazy



# class Home(ListView):
#     model = empleados, areas
#     template_name = 'index.html'
#     context_object_name = 'Cempleados'
#     queryset = empleados.objects.filter(status=True)


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
        object = empleados.objects.get(id = pk)
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

    capacitar = empleados.objects.get(id=pk)

    card = {'card': capacitar}

    return render(request, 'card.html',card)