from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from django.utils import timezone

# 1. Página de inicio (informativa)
def inicio_clientes(request):
    return render(request, 'inicio.html')

# 2. Agregar cliente (mostrando formulario simple y guardando sin forms.py)
def agregar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        empresa = request.POST.get('empresa')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')
        estado = request.POST.get('estado')

        Cliente.objects.create(
            nombre=nombre,
            empresa=empresa,
            correo=correo,
            telefono=telefono,
            direccion=direccion,
            estado=estado
        )
        return redirect('ver_clientes')

    return render(request, 'cliente/agregar_cliente.html')

# 3. Ver clientes (lista)
def ver_clientes(request):
    clientes = Cliente.objects.all().order_by('-fecha_registro')
    return render(request, 'cliente/ver_clientes.html', {'clientes': clientes})

# 4. Mostrar formulario de actualización
def actualizar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente})

# 5. Realizar la actualización (POST)
def realizar_actualizacion_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.empresa = request.POST.get('empresa')
        cliente.correo = request.POST.get('correo')
        cliente.telefono = request.POST.get('telefono')
        cliente.direccion = request.POST.get('direccion')
        cliente.estado = request.POST.get('estado')
        cliente.save()
        return redirect('ver_clientes')
    return redirect('actualizar_cliente', cliente_id=cliente.id)

# 6. Borrar cliente
def borrar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    # opcional: pedir confirmación con una plantilla
    return render(request, 'cliente/confirmar_borrado.html', {'cliente': cliente})