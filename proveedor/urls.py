# proveedor/urls.py

from django.urls import path
from .views import proveedor_list, proveedor_create, proveedor_update, proveedor_delete

urlpatterns = [
    path('', proveedor_list, name='proveedor-list'),  # Asegúrate de que el nombre sea correcto
    path('nuevo/', proveedor_create, name='proveedor-create'),
    path('editar/<int:pk>/', proveedor_update, name='proveedor-update'),
    path('eliminar/<int:pk>/', proveedor_delete, name='proveedor-delete'),
]
