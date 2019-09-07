from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.forms import ModelForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from .form import EmpleadosForm
from .models import empleados
from django.urls import reverse_lazy


class Inicio(TemplateView):
    template_name = 'inicioSesion.html'

def Home(request):
    texto = {
        'texto' : "Home"
    }
    return render(request, 'index.html', texto)


def empleado(request):
    texto = {
        'texto' : "Empleados"
    }
    return render(request, 'empleados.html', texto)


def capacitaciones(request):
    texto = {
        'texto' : "Capacitaciones"
    }
    return render(request, 'capacitaciones.html', texto)

class login(TemplateView):
     template_name = 'login.html'



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

# def eliminarEmpleado(request, id):
#     empleado = empleados.objects.get(id = id)
#     if request.method == 'POST':
#         empleado.status = False
#         empleado.save()
#         return redirect('lista')
#     return render(request, 'empleados_confirm_delete.html', {'empleado': empleado})