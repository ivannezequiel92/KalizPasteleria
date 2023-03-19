from django.shortcuts import render
from AppKaliz.models import Tortas
from django.http import HttpResponse

# Create your views here.

def guardar_tortas(request, peso):
    torta = Tortas(nombre="Selvanegra", peso=peso)
    torta.save()
    return HttpResponse("Postre creado exitosamente")