# backend_agencia_de_marketing/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # RUTA RAÍZ (/)
    # La ruta raíz va a app_clientes.urls.py, donde se define path('', views.inicio_clientes)
    path('', include('app_clientes.urls')), 
    
    # RUTAS DE EMPLEADOS (Se accede a ellas con el prefijo 'empleados/' o 'proyectos/')
    # Si quieres que las rutas de empleados NO tengan prefijo, tienes que
    # mover las rutas de proyectos de app_empleados.urls.py a app_clientes.urls.py o viceversa,
    # o usar dominios distintos.
    
    # Opción 1: Incluir empleados bajo un prefijo (Recomendado)
    path('empleados/', include('app_empleados.urls')),
    
    # Opción 2: Si quieres que app_empleados se incluya en la raíz, debes
    # Mover la línea path('', include('app_clientes.urls')), y ponerla al final
    # o bajo un prefijo (ej: path('clientes/', include('app_clientes.urls'))).
]