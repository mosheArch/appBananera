from surBananas import views
from django.urls import path
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(views.Home.as_view()), name = 'home'),
    path('capacitaciones', login_required(views.crearCapacitacion.as_view()), name = 'capacitaciones'),
    path('addEmpleado', login_required(views.CrearEmpleado.as_view()), name = 'addEmpleado'),
    path('listaCapacitaciones', login_required(views.ListaCapacitacion.as_view()), name = 'listaCapacitaciones'),
    path('listaEmpleado', login_required(views.ListaEmpleado.as_view()), name = 'lista'),
    path('editarEmpleado/<int:pk>', views.ActualizarEmpleado.as_view(), name = 'editarEmpleado'),
    path('editarCapacitaciones/<int:pk>', views.ActualizarCapacitaciones.as_view(), name = 'editarCapacitaciones'),
    path('eliminarEmpleado/<int:pk>', views.EliminarEmpleado.as_view(), name = 'eliminarEmpleado'),
    path('eliminarCapacitaciones/<int:pk>', views.EliminarCapacitaciones.as_view(), name = 'eliminarCapacitaciones'),
    #path('index', views.Inicio.as_view(), name= 'IndexAdmin')

]