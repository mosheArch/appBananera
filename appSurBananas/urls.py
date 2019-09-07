
from django.contrib import admin
from django.urls import path, include
from surBananas.views import Inicio

urlpatterns = [
    #path('accounts/login/', Login.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('bananera/', include('surBananas.urls')),
    path('', Inicio.as_view(), name='index'),

]
