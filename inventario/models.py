from django.db import models
from formularios.validaciones import *

# Create your models here.
class General(models.Model):
    idgenr_general = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre',max_length=50, blank=False, null=False)

    class Meta:
        verbose_name = 'Lista',
        verbose_name_plural = 'Listas',
        db_table = 'General'

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=45, blank=False, null=False,validators=[validate_descripcion])
    cedula = models.CharField(max_length= 45, blank=False, null=False,validators=[validate_cedula])
    placa_carro = models.CharField(max_length=50, blank=False, null=False,validators=[validar_placa])
    descripcion_problema= models.TextField(max_length=200,validators=[validate_descripcion])
    imagen=models.ImageField(max_length=50)
    id_genr_estado = models.ForeignKey(General,on_delete=models.CASCADE, related_name="fk_usuario_estado", db_column='id_genr_estado')

    class Meta:
        verbose_name = 'Usuario',
        verbose_name_plural = 'Usuarios',
        db_table = 'Usuario'

    def __str__(self):
        return self.usuario

class Productos(models.Model):
    id_productos = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario')
    nombre_producto=models.CharField(max_length=50,blank=False, null=False,validators=[validate_descripcion])
    descripcion = models.TextField(max_length=50, blank=False, null=False,validators=[validate_descripcion])
    categoria = models.CharField(max_length=30, blank=False, null=False, validators=[validate_descripcion])
    precio =models.IntegerField( blank=False, null=False,validators=[espacios])
    imagen = models.ImageField(max_length=50)
    fecha_entrada =models.DateField(auto_now=True,blank=False, null=False,validators=[validate_fecha])
    fecha_salida =models.DateField(auto_now_add=True,blank=False, null=False,validators=[validate_fecha])

    class Meta:
        verbose_name = 'producto del usuario',
        verbose_name_plural = 'productos del usuarios',
        db_table = 'Productos'

    def __int__(self):
        return self.id_productos

class Inventarios(models.Model):
    id_inventario=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50,blank=False, null=False,validators=[validate_descripcion])
    descripcion = models.TextField(max_length=50, blank=False, null=False, validators=[validate_descripcion])
    fecha_entrada = models.DateField(auto_now=True,blank=False, null=False, validators=[validate_fecha])
    fecha_salida = models.DateField(auto_now_add=True,blank=False, null=False, validators=[validate_fecha])
    imagen = models.ImageField(max_length=50)

    class Meta:
        verbose_name = 'nombre',
        verbose_name_plural = 'nombre',
        db_table = 'Inventarios'

    def __int__(self):
        return self.id_inventario
