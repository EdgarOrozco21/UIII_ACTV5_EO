from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'empresa', 'correo', 'telefono', 'fecha_registro', 'estado')
    search_fields = ('nombre', 'empresa', 'correo')