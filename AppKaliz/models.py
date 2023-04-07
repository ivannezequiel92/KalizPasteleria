from django.db import models
from django.contrib.auth.models import User



# Create your models here.

# class Tortas(models.Model):
#     nombre = models.CharField(max_length=40)
#     peso = models.FloatField()
#
#     def __str__(self):
#         return f"Torta: {self.nombre}, y su peso es: {self.peso}"



class Recetas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.ForeignKey, null=True, blank=True)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    Duracion = models.IntegerField()
    Receta = models.CharField(max_length=30)
    Descripcion = models.CharField(max_length=50, null=True, blank=True)
    Pasos = models.TextField(null=True, blank=True)
    Imagen = models.ImageField(upload_to="media/ImagenesUsuarios", null=True, blank=True)
    Ingredientes = models.CharField(max_length=200)


    def __str__(self):
        return f"Receta: {self.Receta}, Descripcion {self.Descripcion}, {self.Imagen}"


class RecetasDulces(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.ForeignKey, null=True, blank=True)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    Duracion = models.IntegerField()
    Receta = models.CharField(max_length=30)
    Descripcion = models.CharField(max_length=50, null=True, blank=True)
    Pasos = models.TextField(null=True, blank=True)
    Imagen = models.ImageField(upload_to="media/ImagenesUsuarios", null=True, blank=True)
    Ingredientes = models.CharField(max_length=200)


    def __str__(self):
        return f"Receta: {self.Receta}, Descripcion {self.Descripcion}, {self.Imagen}"


# class Torta(models.Model):
#     nombre = models.CharField(max_length=30)
#     peso = models.FloatField()
#
#     def __str__(self):
#         return f"Torta: {self.nombre}, Peso: {self.peso}"
#
# class Sandwiche(models.Model):
#     tipo = models.CharField(max_length=30)
#     sabor = models.CharField(max_length=30)
#
#     def __str__(self):
#         return f"Sandwiche: {self.tipo}, Sabor: {self.sabor}"

class Comentario(models.Model):
    fechaPublicacion = models.DateTimeField(auto_now=True)
    usuario = models.TextField(max_length=30)
    comentario = models.TextField(max_length=400)

    def __str__(self):
        return f"Usuario: {self.usuario}, comentario: {self.comentario}, Fecha: {self.fechaPublicacion}"



