from django import forms
from django.forms import ModelForm
from core.models import *

class ProductoForms(forms.ModelForm):
    class Meta:
        model = Producto
        fields=[
            'nombre_producto',
            'descripcion',
            'categoria',
            'precio',
            'fecha_entrada',
            'fecha_salida'
        ]
        labels={
            'nombre_producto':'Nombre del producto',
            'descripcion':'Descripción del producto',
            'categoria':'categoria del carro',
            'precio':'precio',
            'fecha_entrada':'Imagen',
            'fecha_salida':'Nombre de la imagen',
        }
        widgets = {
            'nombre_producto':forms.TextInput(attrs={"class":"form-control","placeholder": "Ingrese nombre del producto"}),
            'descripcion':forms.TextInput(attrs={"class":"form-control","placeholder": "Ingrese descripcion"}),
            'categoria':forms.TextInput(attrs={"class":"form-control","placeholder":"categoria"}),
            'precio':forms.TextInput(attrs={"class":"form-control","placeholder":"precio"}),
            'fecha_entrada': forms.DateTimeImput(attrs={"class":"form-control","type":"date"}),
            'fecha_salida': forms.DateTimeImput(attrs={"class": "form-control","type":"date"})
        }
