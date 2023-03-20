
from django import forms

class AlfajoresForm(forms.Form):

    nombre = forms.CharField(min_length=3, max_length=40)
    tipo = forms.CharField(min_length=3, max_length=40)
    sabor = forms.CharField(min_length=3, max_length=40)

class BusquedaAlfajorForm(forms.Form):

    sabor = forms.CharField(min_length=3, max_length=40)

class TortasForm(forms.Form):

    nombre = forms.CharField(min_length=3, max_length=40)
    peso = forms.FloatField()

class BusquedaTortaForm(forms.Form):

    nombre = forms.CharField(min_length=3, max_length=40)



