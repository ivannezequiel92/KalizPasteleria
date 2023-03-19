from django.db import models


# Create your models here.

class Tortas(models.Model):
    nombre = models.CharField(max_length=40)
    peso = models.FloatField()

    def __str__(self):
        return f"Torta: {self.nombre}, y su peso es: {self.peso}"

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField

class Alfajores(models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    sabor = models.CharField(max_length=30)

class Alfajor(models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    sabor = models.CharField(max_length=30)
