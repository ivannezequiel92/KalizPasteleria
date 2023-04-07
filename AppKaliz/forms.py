from django.contrib.auth.models import User
from django import forms
from AppKaliz.models import Recetas, RecetasDulces, Comentario


class RecetasForm(forms.ModelForm):
    class Meta:
       model = Recetas
       fields = (
        'usuario', 'Receta', 'Duracion', 'Descripcion', 'Ingredientes', 'Pasos', 'Imagen')

    widgets = {
           'usuario': forms.TextInput(
               attrs={'class': 'form-control', 'value': '', 'id': 'usuario_id', 'type': 'hidden'}),

    }
    Imagen: forms.ImageField()
    Duracion: forms.DurationField()
    Receta: forms.CharField(max_length=20)
    Descripcion: forms.CharField(max_length=50)
    Pasos: forms.Textarea()
    Ingredientes: forms.Textarea()
class BusquedaRecetasForm(forms.Form):

    Receta = forms.CharField(min_length=3, max_length=40)

# class TortasForm(forms.Form):
#
#     nombre = forms.CharField(min_length=3, max_length=40)
#     peso = forms.FloatField()
#
# class BusquedaTortaForm(forms.Form):
#
#     nombre = forms.CharField(min_length=3, max_length=40)


class SandwichesForm(forms.Form):

    tipo = forms.CharField(min_length=3, max_length=40)
    sabor = forms.CharField(min_length=3, max_length=40)


class RecetasDulcesForm(forms.ModelForm):
    class Meta:
        model = RecetasDulces
        fields = (
        'usuario', 'Receta', 'Duracion', 'Descripcion', 'Ingredientes', 'Pasos', 'Imagen')

    widgets = {
           'usuario': forms.TextInput(
               attrs={'class': 'form-control', 'value': '', 'id': 'usuario_id', 'type': 'hidden'}),

       }
    Imagen: forms.ImageField()
    Duracion: forms.DurationField()
    Receta: forms.CharField(max_length=20)
    Descripcion: forms.CharField(max_length=50)
    Pasos: forms.Textarea()
    Ingredientes: forms.Textarea()
class BusquedaRecetasDulcesForm(forms.Form):

    Receta = forms.CharField(min_length=3, max_length=40)


class Comentarios(forms.Form):

    class Meta:
        model = Comentario
        fields = ("usuario", "comentarios", "fechaPublicacion")

    fechaPublicacion = forms.DateTimeField()
    comentarios = forms.CharField(max_length=400)
    usuario = forms.CharField(max_length=30)

