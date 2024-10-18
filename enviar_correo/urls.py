from django.urls import path
from .views import enviar_correo

urlpatterns = [
    path('', enviar_correo, name='enviar_correo'),  # Ruta principal de la aplicación
]