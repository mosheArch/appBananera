from django.shortcuts import render
from django.http import HttpResponse

def bananera(request):
    texto = {
        'texto' : "Dashboard"
    }
    return render(request, 'index.html', texto)


def empleados(request):
    texto = {
        'texto' : "Empleados"
    }
    return render(request, 'empleados.html', texto)


def capacitaciones(request):
    texto = {
        'texto' : "Capacitaciones"
    }
    return render(request, 'capacitaciones.html', texto)

def login(request):
    return render(request, 'login.html')
