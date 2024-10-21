from django import forms
from .models import Receta
from cliente.models import Cliente
import re  

class RecetaForm(forms.Form):
    id_cliente = forms.ChoiceField(choices=[], widget=forms.Select(attrs={'class': 'form-control'}))
    nombre_doctor = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        # Si se pasa una instancia, la guardamos
        self.instance = kwargs.pop('instance', None)
        super().__init__(*args, **kwargs)
        clientes = Cliente.objects.all()
        if clientes:
            self.fields['id_cliente'].choices = [(str(cliente.id_cliente), cliente.rut) for cliente in clientes]
        else:
            self.fields['id_cliente'].choices = [('', 'Aún no hay clientes disponibles')]

        # Si es una instancia existente, precargamos los valores
        if self.instance:
            self.fields['id_cliente'].initial = str(self.instance.id_cliente.id_cliente)
            self.fields['nombre_doctor'].initial = self.instance.nombre_doctor

    def clean_nombre_doctor(self):
        """ Valida que el campo nombre_doctor sólo contenga letras """
        nombre_doctor = self.cleaned_data['nombre_doctor']
        if not re.match(r'^[a-zA-Z\s]+$', nombre_doctor):
            raise forms.ValidationError('El nombre del doctor sólo debe contener letras y espacios.')
        return nombre_doctor

    def save(self, commit=True):
        # Si no hay instancia, crear una nueva Receta
        if not self.instance:
            self.instance = Receta()

        cliente_id = self.cleaned_data['id_cliente']
        if cliente_id:  # Si hay cliente seleccionado
            self.instance.id_cliente = Cliente.objects.get(id_cliente=int(cliente_id))  # Actualizar id_cliente
        self.instance.nombre_doctor = self.cleaned_data['nombre_doctor']

        # Guardar la instancia de Receta
        if commit:
            self.instance.save()
        return self.instance
