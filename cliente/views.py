from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm

def cliente_list(request):
    clientes = Cliente.objects.all()  # Obtener todos los clientes
    return render(request, 'cliente/cliente_list.html', {'clientes': clientes})

def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente-list')
    else:
        form = ClienteForm()
    return render(request, 'cliente/cliente_form.html', {'form': form})

def cliente_update(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save(instance=cliente)
            return redirect('cliente-list')
    else:
        # Pasamos el cliente existente para precargar el formulario
        form = ClienteForm(initial={
            'rut': cliente.rut,
            'nombre': cliente.nombre,
            'apellido': cliente.apellido,
        })
    return render(request, 'cliente/cliente_form.html', {'form': form})

def cliente_delete(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente-list')
    return render(request, 'cliente/cliente_confirm_delete.html', {'cliente': cliente})
