from django.urls import path
from .views import categoria_list, categoria_create, categoria_update, categoria_delete
from . import views

urlpatterns = [

    path('', categoria_list, name='categoria-list'),
    path('nuevo/', categoria_create, name='categoria-create'),
    path('<int:pk>/editar/', categoria_update, name='categoria-update'),
    path('<int:pk>/eliminar/', categoria_delete, name='categoria-delete'),
]