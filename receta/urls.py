from django.urls import path
from .views import receta_list, receta_create, receta_update, receta_delete

urlpatterns = [
    path('', receta_list, name='receta-list'),
    path('nueva/', receta_create, name='receta-create'),
    path('<int:pk>/editar/', receta_update, name='receta-update'),
    path('<int:pk>/eliminar/', receta_delete, name='receta-delete'),
]
