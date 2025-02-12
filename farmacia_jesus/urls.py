"""
URL configuration for farmacia_jesus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include


import categoria.urls as cat
import cliente.urls as cl
import producto.urls as pd
import proveedor.urls as pv
import receta.urls as rc
from core.views import home 
from enviar_correo.views import enviar_correo

urlpatterns = [
    
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("categorias/", include(cat.urlpatterns)),
    path("clientes/", include(cl.urlpatterns)),
    path("productos/", include(pd.urlpatterns)),
    path("proveedores/", include(pv.urlpatterns)),
    path("recetas/", include(rc.urlpatterns)),
    path("enviar-correo/", enviar_correo, name="enviar_correo"),
    
]
