from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from formularios.forms import *

class CreateFactura(CreateView):
    model = Factura
    form_class = FacturaForms
    template_name = 'factura/crear_factura.html'
    success_url= reverse_lazy('core/base')

class UpdateFactura(UpdateView):
    model = Factura
    form_class = FacturaForms
    context_object_name = 'f'
    template_name = 'factura/editar_factura.html'
    success_url = reverse_lazy('core/base')

class DeleteFactura(DeleteView):
    model = Factura
    form_class = FacturaForms
    context_object_name = 'f'
    template_name = 'factura/eliminar_factura.html'
    success_url = reverse_lazy('core/base')
