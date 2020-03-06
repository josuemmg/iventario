from django import forms
from inventario.models import Productos, Inventarios
from factura.models import *


class ProductoForms(forms.ModelForm):
    class Meta:
        model = Productos
        fields=[
            'nombre_producto',
            'descripcion',
            'categoria',
            'precio',
            'imagen',
            'fecha_entrada',
            'fecha_salida'
        ]
        labels={
            'nombre_producto':'Nombre del producto',
            'descripcion':'Descripción del producto',
            'categoria':'categoria del carro',
            'precio':'precio',
            'imagen':'imagen',
            'fecha_entrada':'',

        }
        widgets = {
            'nombre_producto':forms.TextInput(attrs={"class":"form-control","placeholder": "Ingrese nombre del producto"}),
            'descripcion':forms.TextInput(attrs={"class":"form-control","placeholder": "Ingrese descripcion"}),
            'categoria':forms.TextInput(attrs={"class":"form-control","placeholder":"categoria"}),
            'precio':forms.TextInput(attrs={"class":"form-control","placeholder":"precio"}),
            'imagen':forms.ImageField(attrs={"class":"form-control","placeholder":"ingrese imagen"}),
            'fecha_entrada': forms.DateTimeInput(attrs={"class":"form-control","type":"date"}),

        }

######################################Iventario##################################################

class InventarioForms(forms.ModelForm):
    class Meta:
        model = Inventarios
        fields=[
            'nombre',
            'descripcion',
            'fecha_entrada',
            'imagen'
        ]
        labels={
            'nombre':'Nombre del producto',
            'descripcion':'Descripción del producto',
            'fecha_entrada':'',
            'imagen': 'imagen',

        }
        widgets = {
            'nombre':forms.TextInput(attrs={"class":"form-control","placeholder": "Ingrese nombre del producto"}),
            'descripcion':forms.TextInput(attrs={"class":"form-control","placeholder": "Ingrese descripcion"}),
            'imagen': forms.ImageField(attrs={"class": "form-control", "placeholder": "ingrese imagen"}),
            'fecha_entrada': forms.DateTimeInput(attrs={"class":"form-control","type":"date"}),

        }

#####################################Factura###############################################

class FacturaForms(forms.ModelForm):
    class Meta:
        model = Factura
        fields = [
        'nombre_fact',
        'nombre_usu',
        'nombre_pro',
        'direccion',
        'valor_unitario',
        'cantidad',
        'iva',
        'descuento',
        'fecha_entrada',
        'fecha_salida'

    ]
        labels = {
        'nombre_fact': 'Nombre del producto',
        'nombre_usu': 'Descripción del producto',
        'nombre_pro': 'categoria del carro',
        'direccion': 'precio',
        'valor_unitario': 'imagen',
        'cantidad': '',
        'iva': '',
        'descuento': "",
        'fecha_entrada': ''

        }
        widgets = {
            'nombre_fact':forms.TextInput(attrs={"class":"form-control","placeholder": "Ingrese nombre de la factura"}),
            'nombre_usu':forms.TextInput(attrs={"class":"form-control","placeholder": "Ingrese usuario"}),
            'nombre_pro': forms.ImageField(attrs={"class": "form-control", "placeholder": "ingrese productos"}),
            'direccion':forms.TextInput(attrs={"class":"form-control","placeholder": "Ingrese direccion"}),
            'valor_unitario': forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese valor unitario"}),
            'cantidad': forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese cantidad"}),
            'iva': forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese iva"}),
            'descuento': forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese descuento"}),
            'fecha_entrada': forms.DateTimeInput(attrs={"class": "form-control", "type": "date"}),


        }