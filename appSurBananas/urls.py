
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('surBananas.urls')),
    path('admin/', admin.site.urls),
    path('home/', include('surBananas.urls')),

]
