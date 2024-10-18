from django.urls import path
from .views import cliente_list, cliente_create, cliente_update, cliente_delete
from . import views

urlpatterns = [
    path('', views.cliente_list, name='cliente-list'),
    path('nuevo/', views.cliente_create, name='cliente-create'),
    path('editar/<str:pk>/', views.cliente_update, name='cliente-update'),
    path('eliminar/<str:pk>/', views.cliente_delete, name='cliente-delete'),
]
