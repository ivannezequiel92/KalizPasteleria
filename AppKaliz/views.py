from django.shortcuts import render
from AppKaliz.models import  Alfajor, Torta
from AppKaliz.forms import AlfajoresForm, BusquedaAlfajorForm, BusquedaTortaForm, TortasForm

from django.http import HttpResponse


# Create your views here.

def inicio(request):
    return render(request, "base.html")


def clientes(request):
    pass


def alfajores(request):

    if request.method == "POST":
        mi_formulario = AlfajoresForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            alfajor_save = Alfajor(
                nombre=informacion['nombre'],
                tipo=informacion['tipo'],
                sabor=informacion['sabor'],
            )
            alfajor_save.save()

    all_alfajores = Alfajor.objects.all()
    context = {
        "alfajores": all_alfajores,
        "form": AlfajoresForm(),
        "form_busqueda": BusquedaAlfajorForm()
    }
    return render(request, "AppKaliz/alfajores.html", context=context)

def crear_alfajor(request, nombre, tipo, sabor):
    save_alfajor = Alfajor(nombre=nombre, tipo=tipo, sabor=sabor)
    save_alfajor.save()
    context = {
        "nombre": nombre,

    }
    return render(request, "AppKaliz/guardar_alfajor.html", context)


def busqueda_alfajor(request):
    #mostrar datos filtrados
    mi_formulario = BusquedaAlfajorForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        alfajores_filtrados = Alfajor.objects.filter(sabor__icontains=informacion['sabor'])
        context = {
            "Alfajores": alfajores_filtrados
        }
    return render(request, "AppKaliz/busqueda_alfajor.html", context=context)


def tortas(request):

    if request.method == "POST":
        mi_formulario = TortasForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            torta_save = Torta(
                nombre=informacion['nombre'],
                peso=informacion['peso'],
            )
            torta_save.save()

    all_torta = Torta.objects.all()
    context = {
        "tortas": all_torta,
        "form": TortasForm(),
        "form_busqueda": BusquedaTortaForm()
    }
    return render(request, "AppKaliz/tortas.html", context=context)

def crear_torta(request, nombre, peso):
    save_torta = Torta(nombre=nombre, peso=peso)
    save_torta.save()
    context = {
        "nombre": nombre,

    }
    return render(request, "AppKaliz/guardar_torta.html", context)


def busqueda_torta(request):
    #mostrar datos filtrados
    mi_formulario = BusquedaTortaForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        tortas_filtrados = Torta.objects.filter(nombre__icontains=informacion['nombre'])
        context = {
            "Tortas": tortas_filtrados
        }
    return render(request, "AppKaliz/busqueda_torta.html", context=context)
