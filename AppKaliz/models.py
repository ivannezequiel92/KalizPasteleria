from django.db import models


# Create your models here.

class Tortas(models.Model):
    nombre = models.CharField(max_length=40)
    peso = models.FloatField()

    def __str__(self):
        return f"Torta: {self.nombre}, y su peso es: {self.peso}"



class Alfajores(models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    sabor = models.CharField(max_length=30)

    def __str__(self):
        return f"Alfajor: {self.nombre}, Tipo: {self.tipo}, Sabor: {self.sabor}"
class Alfajor(models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    sabor = models.CharField(max_length=30)

    def __str__(self):
        return f"Alfajor: {self.nombre}, Tipo: {self.tipo}, Sabor: {self.sabor}"

class Torta(models.Model):
    nombre = models.CharField(max_length=30)
    peso = models.FloatField()

    def __str__(self):
        return f"Torta: {self.nombre}, Peso: {self.peso}"

class Sandwiche(models.Model):
    tipo = models.CharField(max_length=30)
    sabor = models.CharField(max_length=30)

    def __str__(self):
        return f"Sandwiche: {self.tipo}, Sabor: {self.sabor}"