from django.db import models

# Create your models here.
class General(models.Model):
    idgenr_general = models.AutoField(primary_key=True)
    placa = models.CharField('Placa',max_length=50, blank=False, null=False)
    nombre = models.CharField('Nombre',max_length=50, blank=False, null=False)

    class Meta:
        verbose_name = 'Lista',
        verbose_name_plural = 'Listas',
        db_table = 'General'

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=45, blank=False, null=False)
    cedula = models.CharField(max_length= 45, blank=False, null=False)
    placa_carro = models.CharField(max_length=50, blank=False, null=False)
    descripcion_problema= models.TextField(max_length=200)
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
    precio =models.IntegerField( blank=False, null=False)
    imagen = models.ImageField(max_length=50)
    fecha_entrada =models.DateField(blank=False, null=False)
    fecha_salida =models.DateField(blank=False, null=False)

    class Meta:
        verbose_name = 'producto del usuario',
        verbose_name_plural = 'productos del usuarios',
        db_table = 'Productos'

    def __int__(self):
        return self.id_productos
