# app_empleados/urls.py
from django.urls import path
from . import views

# Todas las vistas de Proyectos y Empleados deben estar definidas en views.py
urlpatterns = [
    # Rutas de Proyectos
    path('proyectos/ver/', views.ver_proyectos, name='ver_proyectos'),
    path('proyecto/nuevo/', views.agregar_proyecto, name='proyecto_nuevo'), 
    path('proyecto/<int:pk>/detalle/', views.proyecto_detalle, name='proyecto_detalle'),
    path('proyecto/<int:pk>/editar/', views.proyecto_editar, name='proyecto_editar'),
    path('proyecto/<int:pk>/borrar/', views.proyecto_borrar, name='proyecto_borrar'),
    
    # ----------------------------------------------------------------------
    # Rutas de Empleados
    # ----------------------------------------------------------------------
    path('empleado/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleados/ver/', views.ver_empleados, name='ver_empleados'),
    
    # Detalle de Empleado 
    path('empleado/<int:pk>/detalle/', views.empleado_detalle, name='empleado_detalle'),
    
    # Edición y Eliminación de Empleado
    # 🌟 CORREGIDO: El nombre ahora es 'empleado_editar' para coincidir con el HTML
    path('empleado/<int:pk>/editar/', views.empleado_editar, name='empleado_editar'), 
    
    # 🌟 CORREGIDO: Se cambia el nombre para usar 'eliminar_empleado' como en el HTML
    path('empleado/<int:pk>/eliminar/', views.eliminar_empleado, name='eliminar_empleado'), 
]