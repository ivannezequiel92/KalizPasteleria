from django.shortcuts import render
from AppKaliz.models import  Alfajor, Tortas

from django.http import HttpResponse


# Create your views here.

def inicio(request):
    return render(request, "base.html")


def clientes(request):
    pass


def alfajores(request):
    all_alfajores = Alfajor.objects.all()
    context = {
        "alfajores": all_alfajores
    }
    return render(request, "AppKaliz/alfajores.html", context=context)

def crear_alfajor(request, nombre, tipo, sabor):
    save_alfajor = Alfajor(nombre=nombre, tipo=tipo, sabor=sabor)
    save_alfajor.save()
    context = {
        "nombre": nombre,

    }
    return render(request, "AppKaliz/guardar_alfajor.html", context)

def tortas(request):
    all_tortas= Tortas.objects.all()
    context = {
        "tortas": all_tortas
    }
    return render(request, "AppKaliz/tortas.html", context=context)