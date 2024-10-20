from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['id_producto', 'id_proveedor', 'id_categoria', 'nombre', 'precio_unitario']
        widgets = {
            'id_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'id_proveedor': forms.Select(attrs={'class': 'form-control'}),
            'id_categoria': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_unitario': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        