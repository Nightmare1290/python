from django.db import models

# Create your models here.
class user(models.Model):
    nombre = models.CharField
    correo = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)
    cartera = models.CharField(max_length=20)

class promocion(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    imagen = models.CharField(max_length=50)
    vigencia = models.CharField(max_length=30)
    sublineas = models.CharField(max_length=40)
    dirigido = models.CharField(max_length=40)
    restricciones = models.CharField(max_length=200)
    avances = models.CharField(max_length=100)
    descuento = models.CharField(max_length=20)
    cartera = models.CharField(max_length=20)


class concurso(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    imagen = models.CharField(max_length=50)
    vigencia = models.CharField(max_length=30)
    dirigido = models.CharField(max_length=40)
    sublineas = models.CharField(max_length=40)
    restricciones = models.CharField(max_length=200)
    cartera = models.CharField(max_length=20)