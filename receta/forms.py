from django import forms
from .models import Receta
from cliente.models import Cliente

class RecetaForm(forms.Form):
    id_cliente = forms.ChoiceField(choices=[], widget=forms.Select(attrs={'class': 'form-control'}))
    nombre_doctor = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        # Si se pasa una instancia, la guardamos
        self.instance = kwargs.pop('instance', None)
        super().__init__(*args, **kwargs)
        
        # Poblar el campo de id_cliente con opciones desde mongoengine
        clientes = Cliente.objects.all()
        self.fields['id_cliente'].choices = [(str(cliente.id_cliente), cliente.rut) for cliente in clientes]

        # Si es una instancia existente, precargamos los valores
        if self.instance:
            self.fields['id_cliente'].initial = str(self.instance.id_cliente.id_cliente)
            self.fields['nombre_doctor'].initial = self.instance.nombre_doctor

    def save(self, commit=True):
        # Si no hay instancia, crear una nueva Receta
        if not self.instance:
            self.instance = Receta()

        cliente_id = self.cleaned_data['id_cliente']
        self.instance.id_cliente = Cliente.objects.get(id_cliente=int(cliente_id))  # Actualizar id_cliente
        self.instance.nombre_doctor = self.cleaned_data['nombre_doctor']

        # Guardar la instancia de Receta
        if commit:
            self.instance.save()
        return self.instance