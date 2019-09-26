
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from surBananas.views import Dashboard
from usuarios.views import Login, salirUsuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bananera/', include(('surBananas.urls'))),
    path('', login_required(Dashboard), name='index'),
    path('accounts/login/', Login.as_view(), name = 'LogIn'),
    path('logout/', login_required(salirUsuario), name = 'salir'),
]

admin.site.site_header = 'Surbananas Administrador'
