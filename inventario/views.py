from formularios.forms import *
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *

##################Productos##########################
class CreateProducto(CreateView):
    model = Productos
    form_class = ProductoForms
    template_name = 'productos/crear_productos.html'
    success_url= reverse_lazy('producto')

class UpdateProducto(UpdateView):
    model = Productos
    form_class = ProductoForms
    context_object_name = 'p'
    template_name = 'productos/editar_producto.html'
    success_url = reverse_lazy('producto')

class DeleteProducto(DeleteView):
    model = Productos
    form_class = ProductoForms
    context_object_name = 'p'
    template_name = 'productos/eliminar_producto.html'
    success_url = reverse_lazy('producto')

##################inventario##########################
class CreateIventario(CreateView):
    model = Inventarios
    form_class = InventarioForms
    template_name = 'iventario/insertar.html'
    success_url= reverse_lazy('base')

class UpdateIventario(UpdateView):
    model = Productos
    form_class = InventarioForms
    context_object_name = 'I'
    template_name = 'iventario/editar.html'
    success_url = reverse_lazy('base')

class DeleteIventario(DeleteView):
    model = Productos
    form_class = InventarioForms
    context_object_name = 'I'
    template_name = 'iventario/eliminar.html'
    success_url = reverse_lazy('base')