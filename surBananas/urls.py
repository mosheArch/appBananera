from surBananas import views
from django.urls import path

urlpatterns = [
    path('bananera', views.bananera, name = 'bananera'),
    path('empleados', views.empleados, name = 'empleados'),
    path('capacitaciones', views.capacitaciones, name = 'capacitaciones'),
    path('', views.login, name='login'),
]