from django.shortcuts import render
from formularios.forms import *
from .models import *
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def inventario(request):
    dicc={}
    inventario=iventario.objects.all()
    dicc['inventario']=inventario
    if request.method=='POST':
       pass
    return render (request,'base/base.html',dicc)

##################Productos##########################

class CreateProducto(CreateView):
    model = Producto
    form_class = ProductoForms
    template_name = 'productos/crear_productos.html'
    success_url= reverse_lazy('producto')

class UpdateProducto(UpdateView):
    model = Producto
    form_class = ProductoForms
    context_object_name = 'p'
    template_name = 'productos/editar_producto.html'
    success_url = reverse_lazy('producto')

class DeleteProducto(DeleteView):
    model = Producto
    form_class = ProductoForms
    context_object_name = 'p'
    template_name = 'productos/eliminar_producto.html'
    success_url = reverse_lazy('producto')

