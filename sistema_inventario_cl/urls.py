from django.contrib import admin
from django.urls import path
from Apps import views
from factura.views import *
from inventario.views import *
from views import *

urlpatterns = [
   # path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('sample/', views.sample, name="sample"),
    path('bienvenido/', views.bienvenido, name="bienvenido"),
    path('desarrollo/', views.desarrollo, name="desarrollo"),
    path('diseño/', views.diseño, name="diseño"),

    ##################producto################################
    path('crear/',CreateProducto.as_view(),name='producto_create'),
    path('editar/<int:pk>',UpdateProducto.as_view(), name="producto_editar"),
    path('eliminar/<int:pk>', DeleteProducto.as_view(), name="producto_eliminar"),

    ##################inventario#############################
    path('crear_inve/',CreateIventario.as_view(),name="crear_inventario"),
    path('editar_inve/<int:pk>', UpdateProducto.as_view(), name="inventario_editar"),
    path('eliminar_inve/<int:pk>', DeleteProducto.as_view(), name="inventario_eliminar"),

    ##################factura####################################
    path('crear_fact/',CreateFactura.as_view(),name="crear_factura"),
    path('editar_fact/<int:pk>', UpdateFactura.as_view(), name="factura_editar"),
    path('eliminar_fact/<int:pk>', DeleteFactura.as_view(), name="factura_eliminar"),

]