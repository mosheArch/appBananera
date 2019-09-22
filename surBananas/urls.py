from surBananas import views
from django.urls import path
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(views.Home.as_view()), name = 'home'),
    path('capacitaciones', login_required(views.crearCapacitacion.as_view()), name = 'capacitaciones'),
    path('addEmpleado', login_required(views.CrearEmpleado.as_view()), name = 'addEmpleado'),
    path('agregarArea', login_required(views.CrearArea.as_view()), name = 'crearArea'),
    path('listaCapacitaciones', login_required(views.ListaCapacitacion.as_view()), name = 'listaCapacitaciones'),
    path('listaAreas', login_required(views.ListaArea.as_view()), name = 'listaAreas'),
    path('listaEmpleado', login_required(views.ListaEmpleado.as_view()), name = 'lista'),
    path('editarEmpleado/<int:pk>', views.ActualizarEmpleado.as_view(), name = 'editarEmpleado'),
    path('editarCapacitaciones/<int:pk>', views.ActualizarCapacitaciones.as_view(), name = 'editarCapacitaciones'),
    path('editarAreas/<int:pk>', views.ActualizarAreas.as_view(), name = 'editarAreas'),
    path('eliminarEmpleado/<int:pk>', views.EliminarEmpleado.as_view(), name = 'eliminarEmpleado'),
    path('eliminarCapacitaciones/<int:pk>', views.EliminarCapacitaciones.as_view(), name = 'eliminarCapacitaciones'),
    path('eliminarAreas/<int:pk>', views.EliminarArea.as_view(), name = 'eliminarAreas'),
    #path('index', views.Inicio.as_view(), name= 'IndexAdmin')

]