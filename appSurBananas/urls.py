
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from surBananas.views import Dashboard
from usuarios.views import Login, salirUsuario
from django.conf.urls.static import static
#from ctypes.test.test_pickling import name
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bananera/', include(('surBananas.urls'))),
    path('', login_required(Dashboard), name='index'),
    path('accounts/login/', Login.as_view(), name = 'LogIn'),
    path('logout/', login_required(salirUsuario), name = 'salir'),
    path('summernote/', include('django_summernote.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Surbananas Administrador'
