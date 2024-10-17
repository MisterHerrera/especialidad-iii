from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm  # Asegúrate de tener un formulario para manejar la creación y actualización

def producto_list(request):
    productos = Producto.objects.all()  # Obtiene todos los productos
    return render(request, 'producto/producto_list.html', {'productos': productos})

def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto-list')
    else:
        form = ProductoForm()
    return render(request, 'producto/producto_form.html', {'form': form})

def producto_update(request, pk):
    producto = Producto.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto-list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'producto/producto_form.html', {'form': form})

def producto_delete(request, pk):
    producto = Producto.objects.get(pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('producto-list')
    return render(request, 'producto/producto_confirm_delete.html', {'producto': producto})
