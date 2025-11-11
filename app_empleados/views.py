# app_empleados/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado, Proyecto 
from .forms import EmpleadoForm, ProyectoForm 
from django.db.models import Count 
from django.urls import reverse_lazy 
from django.views.generic import CreateView, UpdateView, DeleteView 


# ------------------------------------
# 1. Vistas de Proyectos
# ------------------------------------

def ver_proyectos(request):
    """Muestra la lista de todos los proyectos."""
    # Corregido: Usa Count y pasa como 'object_list'
    proyectos = Proyecto.objects.all().annotate(num_empleados=Count('empleados'))
    return render(request, 'proyectos/lista_proyectos.html', {'object_list': proyectos})

def agregar_proyecto(request):
    """Permite agregar un nuevo proyecto."""
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('ver_proyectos')
    else:
        form = ProyectoForm()
    
    return render(request, 'proyectos/agregar_proyecto.html', {'form': form})

def proyecto_detalle(request, pk):
    """Muestra el detalle de un proyecto específico."""
    proyecto = get_object_or_404(Proyecto, pk=pk)
    return render(request, 'proyectos/proyecto_detalle.html', {'proyecto': proyecto})

def proyecto_editar(request, pk):
    """Permite editar un proyecto existente."""
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('proyecto_detalle', pk=pk)
    else:
        form = ProyectoForm(instance=proyecto)
    
    # Corregido: Pasa el objeto 'proyecto' para que la plantilla pueda crear enlaces
    return render(request, 'proyectos/proyecto_form.html', {'form': form, 'proyecto': proyecto})

def proyecto_borrar(request, pk):
    """Permite eliminar un proyecto."""
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == 'POST':
        proyecto.delete()
        return redirect('ver_proyectos')
    return render(request, 'proyectos/proyecto_confirm_delete.html', {'proyecto': proyecto})


# ------------------------------------
# 2. Vistas de Empleados
# ------------------------------------

def agregar_empleado(request):
    """Permite agregar un nuevo empleado."""
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_empleados')
    else:
        form = EmpleadoForm()
    
    return render(request, 'empleados/agregar_empleado.html', {'form': form, 'titulo': 'Agregar Empleado'})

def ver_empleados(request):
    """Muestra la lista de todos los empleados."""
    empleados = Empleado.objects.all()
    return render(request, 'empleados/ver_empleados.html', {'empleados': empleados})

def empleado_detalle(request, pk):
    """Muestra el detalle de un empleado específico. (Nuevo para solucionar NoReverseMatch)"""
    empleado = get_object_or_404(Empleado, pk=pk)
    # Asume que tienes un template llamado 'empleados/empleado_detalle.html'
    return render(request, 'empleados/empleado_detalle.html', {'empleado': empleado})

def empleado_editar(request, pk):
    """Permite editar un empleado existente."""
    empleado = get_object_or_404(Empleado, pk=pk)
    
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado) 
        if form.is_valid():
            form.save()
            return redirect('ver_empleados') 
    else:
        form = EmpleadoForm(instance=empleado) 
        
    return render(request, 'empleados/agregar_empleado.html', {'form': form, 'titulo': 'Editar Empleado'})

def eliminar_empleado(request, pk):
    """Permite eliminar un empleado."""
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleados')
    return render(request, 'empleados/eliminar_empleado.html', {'empleado': empleado})