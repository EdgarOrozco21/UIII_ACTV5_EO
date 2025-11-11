from django.db import models

# ==========================================================
# MODELO EMPLEADO
# ==========================================================
class Empleado(models.Model):
    # Campos basados en EmpleadoForm
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    fecha_contratacion = models.DateField()
    email = models.EmailField(unique=True)
    
    # ⭐ NUEVOS CAMPOS AÑADIDOS
    telefono = models.CharField(max_length=15, blank=True, null=True) # Se permite vacío
    salario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True) # Salario como Decimal
    area = models.CharField(max_length=100, default='Sin Asignar') # Área de trabajo

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        # Puedes añadir un ordering, ej: ordering = ['apellido', 'nombre']

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.cargo})"

# ==========================================================
# MODELO PROYECTO
# ==========================================================
class Proyecto(models.Model):
    # Opciones para el campo 'estado'
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('En Progreso', 'En Progreso'),
        ('Completado', 'Completado'),
        ('Cancelado', 'Cancelado'),
    ]

    # Campos simples
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin_estimada = models.DateField()
    estado = models.CharField(
        max_length=20, 
        choices=ESTADO_CHOICES, 
        default='Pendiente'
    )
    
    # ⭐ Relación con Empleado (ManyToMany): Permite que el proyecto tenga N empleados.
    # El campo 'empleados' se maneja automáticamente con forms.ModelForm.
    empleados = models.ManyToManyField(
        Empleado, 
        related_name='proyectos',
        # Si quieres que el campo en el formulario sea opcional, añade blank=True
        # Si no lo añades, Django asume que es obligatorio.
        # blank=True
    )

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __str__(self):
        return self.nombre