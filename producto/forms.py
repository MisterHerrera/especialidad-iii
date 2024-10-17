from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['id_producto', 'id_proveedor', 'id_categoria', 'nombre', 'precio_unitario']
        