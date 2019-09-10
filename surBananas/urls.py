from surBananas import views
from django.urls import path
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('home', login_required(views.Home.as_view()), name = 'home'),
    path('capacitaciones', views.capacitaciones, name = 'capacitaciones'),
    path('addEmpleado', views.CrearEmpleado.as_view(), name = 'addEmpleado'),
    path('listaEmpleado', views.ListaEmpleado.as_view(), name = 'lista'),
    path('editarEmpleado/<int:pk>', views.ActualizarEmpleado.as_view(), name = 'editarEmpleado'),
    path('eliminarEmpleado/<int:pk>', views.EliminarEmpleado.as_view(), name = 'eliminarEmpleado'),
    path('index', views.Inicio.as_view(), name= 'IndexAdmin')

]