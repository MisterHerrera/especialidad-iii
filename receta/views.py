from django.shortcuts import render, redirect, get_object_or_404
from .models import Receta
from .forms import RecetaForm
from mongoengine.errors import DoesNotExist
def receta_list(request):
    recetas = Receta.objects.all()  # Obtener todas las recetas
    return render(request, 'receta/receta_list.html', {'recetas': recetas})

def receta_create(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('receta-list')
    else:
        form = RecetaForm()
    return render(request, 'receta/receta_form.html', {'form': form})

def receta_update(request, pk):
    try:
        # Obtener la receta por su id_receta
        receta = Receta.objects.get(id_receta=pk)
    except DoesNotExist:
        return redirect('receta-list')  # Redirigir a la lista si no se encuentra la receta
    
    if request.method == 'POST':
        form = RecetaForm(request.POST, instance=receta)
        if form.is_valid():
            form.save()
            return redirect('receta-list')  # Redirige a la lista de recetas después de guardar
    else:
        form = RecetaForm(instance=receta)  # Pasa la receta existente al formulario
    
    return render(request, 'receta/receta_form.html', {'form': form})
def receta_delete(request, pk):
    receta = Receta.objects.get(pk=pk)
    if request.method == 'POST':
        receta.delete()
        return redirect('receta-list')
    return render(request, 'receta/receta_confirm_delete.html', {'receta': receta})
