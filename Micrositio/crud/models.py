from django.db import models

# Create your models here.
class user(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)
    cartera = models.CharField(max_length=20)


class promocion(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    vigencia = models.CharField(max_length=30)
    sublineas = models.CharField(max_length=40)
    dirigido = models.CharField(max_length=40)
    restricciones = models.CharField(max_length=200)
    avances = models.CharField(max_length=100)
    descuento = models.CharField(max_length=20)
    cartera = models.CharField(max_length=20)

    def __unicode__(self,):
        return self.nombre


class concurso(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    vigencia = models.CharField(max_length=30)
    dirigido = models.CharField(max_length=40)
    sublineas = models.CharField(max_length=40)
    restricciones = models.CharField(max_length=200)
    cartera = models.CharField(max_length=20)

    def __unicode__(self,):
        return self.nombre


class promocionImage(models.Model):
    promocion_id = models.ForeignKey(promocion, related_name='images')
    image = models.ImageField(upload_to='promocion/images/')

    def __unicode__(self,):
        return str(self.image)


class concursoImage(models.Model):
    concurso_id=models.ForeignKey(concurso, related_name='images')
    image = model.ImageField(upload_to='concurso/images/')

    def __unicode__(self,):
        return str(self.image)


class Client(models.Model):
    sucursal = models.CharField(max_length=5)
    cartera = models.CharField(max_length=6)
    clientes = models.CharField(max_length=150)
    fecha_alta = models.CharField(max_length=10, default='')
    saldo = models.FloatField()

    def __str__(self):
        return self.clientes