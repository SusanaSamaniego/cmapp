from django.db import models

# Create your models here.
class Encargado(models.Model):
    image = models.ImageField(upload_to="images_encargado")
    nombres = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50, blank=True)
    titulo = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=50, blank=True, null=True)
    cedula_profesional = models.CharField(max_length=8)
    cedula_especialidad = models.CharField(max_length=8)
    registro_ssa = models.CharField(max_length=8)

    class Meta(object):
        verbose_name_plural = 'encargado'

    def __str__(self):
        return self.nombres


class Secretaria(models.Model):
  
    image = models.ImageField(upload_to="image_secretaria")
    nombres = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50, blank=True)
    telefono_personal = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nombres


class Cliente(models.Model):
    image = models.ImageField(upload_to="image_cliente")
    presupuesto=models.BigIntegerField
    nºss=models.BigIntegerField
    NIF=models.BigIntegerField
    nombre = models.CharField(max_length=150)
    apellido= models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)
    telefono_personal = models.IntegerField()
   

    def __str__(self):
        return self.nombre


class Empresa(models.Model):
    empleado = models.ManyToManyField('empleado')
    descripcion = models.CharField(max_length=50)
    direccion = models.TextField()
    jefe_de_producción=models.ManyToOneRel
    productos=models.ManyToManyField
    precio=models.BinaryField
    image = models.ImageField(upload_to="images_empresa")

    def __str__(self):
        return self.descripcion


class Horario(models.Model):
   
    DIA_DOMINGO = 'DO'
    DIA_LUNES = 'LU'
    DIA_MARTES = 'MA'
    DIA_MIERCOLES = 'MI'
    DIA_JUEVES = 'JU'
    DIA_VIERNES = 'VI'
    DIA_SABADO = 'SA'
    DIA_SEMANA_CHOICES = (
        (DIA_DOMINGO, 'Domingo'),
        (DIA_LUNES, 'Lunes'),
        (DIA_MARTES, 'Martes'),
        (DIA_MIERCOLES, 'Miercoles'),
        (DIA_JUEVES, 'Jueves'),
        (DIA_VIERNES, 'Viernes'),
        (DIA_SABADO, 'Sabado'),
    )
    dia_semana = models.CharField(
        max_length=2,
        choices=DIA_SEMANA_CHOICES,
        default=DIA_LUNES,
    )
    hora_inicio = models.TimeField()
    hara_fin = models.TimeField()

    def __str__(self):
        return self.dia_semana




 #   




class Compra (models.Model):
    precio=models.AutoField
    pago=models.BinaryField
    comprador=models.OneToOneField
    producto=models.aggregates



class Empleado(models.Model):
        image = models.ImageField(upload_to="image_empleado")
        dni=models.BigIntegerField
        sueldo=models.BigIntegerField
        nºss=models.BigIntegerField
        telefono=models.BinaryField
        email=models.BinaryField
        direccion=models.BinaryField  
        nombre=models.TextField(max_length=30)
        apellido=models.TextField(max_length=30)


class Empleador(models.Model):
        image = models.ImageField(upload_to="image_empleador")
        sueldo=models.BigIntegerField
        nºss=models.BigIntegerField
        dni=models.BigIntegerField
        telefono=models.BinaryField
        email=models.BinaryField
        direccion=models.BinaryField 
        nombre=models.TextField(max_length=30)
        apellido=models.TextField(max_length=30)
        

class Vendedor(models.Model):
        image = models.ImageField(upload_to="image_vendedor")
        NIF=models.BigIntegerField
        telefono=models.BinaryField
        email=models.BinaryField
        direccion=models.BinaryField  
        sector=models.TextField
        name=models.TextField(max_length=40)
class Comprador(models.Model):
        image = models.ImageField(upload_to="image_comprador")
        NIF=models.BigIntegerField
        sueldo=models.BigIntegerField
        nºss=models.BigIntegerField
        telefono=models.BinaryField
        email=models.BinaryField
        direccion=models.BinaryField  
        targeta_de_credito=models.BinaryField  
        name=models.TextField(max_length=40)      


class Producto(models.Model):
     codigo =models.CharField(max_length=20, unique=True)
     codigo_barra =models.CharField(max_length=20)

     image = models.ImageField(upload_to="image_producto")
     categoria=models.ManyToManyField
     nombre=models.TextField
     referencia=models.AutoField
     descripcion=models.CharField(max_length=20)
     vendedor=models.OneToOneField
     comprador=models.ManyToManyField

