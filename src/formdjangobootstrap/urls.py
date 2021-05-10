from django.contrib import admin
from django.urls import path, include #include

urlpatterns = [
    path('admin/', admin.site.urls),
    #incluir o path da api no diretório do app fdBoots
    path('api/', include('fdBoots.urls'))
]
