from django.db import models
from formularios.validaciones import *

class Factura(models.Model):
    id_factura=models.AutoField(primary_key=True)
    nombre_fact=models.CharField(max_length=30,blank=False,null=False,validators=[validate_descripcion])
    nombre_usu=models.CharField(max_length=30,blank=False,null=False,validators=[validate_descripcion])
    nombre_pro = models.CharField(max_length=45, blank=True, null=True, validators=[validate_descripcion])
    direccion=models.TextField(max_length=45, blank=True, null=True, validators=[validate_descripcion])
    valor_unitario=models.DecimalField(blank=True, null=True, validators=[validate_descripcion])
    cantidad=models.IntegerField(blank=True, null=True, validators=[validate_descripcion])
    iva=models.DecimalField(blank=True, null=True, validators=[validate_descripcion])
    descuento=models.DecimalField(blank=True, null=True, validators=[validate_descripcion])
    fecha_entrada = models.DateField(auto_now=True, blank=False, null=False, validators=[validate_fecha])
    fecha_salida = models.DateField(auto_now_add=True, blank=False, null=False, validators=[validate_fecha])

class Detalle(models.Model):
    id_detalle=models.AutoField(primary_key=True)
    id_factura=models.ForeignKey(Factura, on_delete=models.CASCADE, blank=False, null=False)
    nombre_det=models.CharField(max_length=30,blank=False,null=False,validators=[validate_descripcion])
