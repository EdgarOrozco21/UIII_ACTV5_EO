from django.db import models

# Modelo existente para Clientes
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    correo = models.CharField(max_length=100, unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    fecha_registro = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} ({self.empresa})"

# ------------------------------------------------------------------
# NUEVO MODELO para la Gestión Dinámica de la Imagen de Portada (Media)
# ------------------------------------------------------------------
class Portada(models.Model):
    # Campo para almacenar la referencia al archivo de imagen subido
    # 'upload_to' define la subcarpeta dentro de MEDIA_ROOT donde se guardará
    nombre = models.CharField(max_length=100, default='Portada Principal', unique=True)
    imagen = models.ImageField(upload_to='portadas/', verbose_name='Imagen de Portada') 

    def __str__(self):
        return self.nombre