
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from surBananas.views import Inicio, Home
from usuarios.views import Login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bananera/', include('surBananas.urls')),
    path('', login_required(Home.as_view()), name='index'),
    path('accounts/login/', Login.as_view(), name='login'),
    #path('',auth_login, {'template_name': 'inicioSesion.html'}, name = 'login')
]
