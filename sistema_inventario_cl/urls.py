"""sistema_inventario_cl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from inventario.view import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inventario, name='inventario'),
    ##################producto################################
    path('crear/',CreatePorducto.as_view(),name='producto_create'),
    path('editar/<int:pk>',UpdateProducto.as_view(), name="producto_editar"),
    path('eliminar/<int:pk>', DeleteProducto.as_view(), name="producto_eliminar"),

]
