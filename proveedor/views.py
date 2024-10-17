from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor
from .forms import ProveedorForm

def proveedor_list(request):
    # Obtener todos los proveedores
    proveedores = Proveedor.objects.all()
    # Renderizar la plantilla con la lista de proveedores
    return render(request, 'proveedor/proveedor_list.html', {'proveedores': proveedores})

def proveedor_create(request):
    if request.method == 'POST':
        # Crear un formulario con los datos enviados
        form = ProveedorForm(request.POST)
        if form.is_valid():
            # Guardar el nuevo proveedor
            form.save()
            # Redirigir a la lista de proveedores
            return redirect('proveedor-list')
    else:
        # Crear un formulario vacío
        form = ProveedorForm()
    # Renderizar la plantilla del formulario
    return render(request, 'proveedor/proveedor_form.html', {'form': form})

def proveedor_update(request, pk):
    # Obtener el proveedor específico por su clave primaria
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        # Crear un formulario con los datos enviados, incluyendo el proveedor existente
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            # Guardar los cambios
            form.save()
            # Redirigir a la lista de proveedores
            return redirect('proveedor-list')
    else:
        # Crear un formulario con los datos del proveedor existente
        form = ProveedorForm(instance=proveedor)
    # Renderizar la plantilla del formulario
    return render(request, 'proveedor/proveedor_form.html', {'form': form})

def proveedor_delete(request, pk):
    # Obtener el proveedor específico por su clave primaria
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        # Eliminar el proveedor
        proveedor.delete()
        # Redirigir a la lista de proveedores
        return redirect('proveedor-list')
    # Renderizar la plantilla de confirmación de eliminación
    return render(request, 'proveedor/proveedor_confirm_delete.html', {'proveedor': proveedor})
