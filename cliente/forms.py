from django import forms
from .models import Cliente
import re
from django.core.exceptions import ValidationError

# Validar Rut xd
def validar_rut(value):
    rut_pattern = re.compile(r'^\d{1,8}-[0-9kK]$')
    if not rut_pattern.match(value):
        raise ValidationError('El RUT ingresado no es válido. Debe seguir el formato XXXXXXXX-Y.')

# Validador de nombre y apellido para que solo contenga letras
def validar_texto(value):
    if not value.isalpha():
        raise ValidationError('Este campo solo debe contener letras.')

class ClienteForm(forms.Form):
    rut = forms.CharField(validators=[validar_rut], max_length=10)
    nombre = forms.CharField(validators=[validar_texto], max_length=100)
    apellido = forms.CharField(validators=[validar_texto], max_length=100)

    def save(self, commit=True, instance=None):
        # Si no se pasa una instancia, se crea un nuevo cliente
        if instance is None:
            instance = Cliente()
        
        instance.rut = self.cleaned_data['rut']
        instance.nombre = self.cleaned_data['nombre']
        instance.apellido = self.cleaned_data['apellido']
        
        if commit:
            instance.save()
        return instance
