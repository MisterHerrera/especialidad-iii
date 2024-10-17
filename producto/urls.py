from django.urls import path
from .views import producto_list, producto_create, producto_update, producto_delete

urlpatterns = [
    path('', producto_list, name='producto-list'),  # Esta URL debe ser correcta
    path('nuevo/', producto_create, name='producto-create'),
    path('editar/<int:pk>/', producto_update, name='producto-update'),
    path('eliminar/<int:pk>/', producto_delete, name='producto-delete'),
]
