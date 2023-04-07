from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from AppKaliz.models import Recetas, RecetasDulces, Comentario
from AppKaliz.forms import Comentarios, RecetasForm, BusquedaRecetasForm,  SandwichesForm, RecetasDulcesForm, RecetasDulces, BusquedaRecetasDulcesForm
from django.views.generic import DetailView


from django.http import HttpResponse


# Create your views here.


def inicio(request):
    return render(request, "base.html")


def recetas(request):

    if request.method == "POST":
        mi_formulario = RecetasForm(request.POST, request.FILES)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            receta_save = Recetas(

                Receta=informacion['Receta'],
                Descripcion=informacion['Descripcion'],
                Duracion=informacion['Duracion'],
                usuario=informacion['usuario'],
                Pasos=informacion['Pasos'],
                Imagen=informacion['Imagen'],
                Ingredientes=informacion['Ingredientes'],

                            )
            receta_save.save()

    all_recetas = Recetas.objects.all()
    context = {
        "recetas": all_recetas,
        "form": RecetasForm(),
        "form_busqueda": BusquedaRecetasForm()
    }
    return render(request, "AppKaliz/recetas.html", context=context)

@login_required(login_url='accountRegister')
class CrearReceta(LoginRequiredMixin):
    @login_required(login_url='accountRegister')
    def crear_receta(request, fechaPublicacion, Duracion, usuario, Receta, Pasos,
                     Descripcion, Imagen, Ingredientes):

        save_receta = Recetas(fechaPublicacion=fechaPublicacion, Duracion=Duracion, usuario=usuario,
                              Receta=Receta, Descripcion=Descripcion, Pasos=Pasos,
                              Imagen=Imagen, Ingredientes=Ingredientes )
        save_receta.save()
        context = {
            "Receta": Receta,

        }
        return render(request, HttpResponse, "AppKaliz/guardar_receta.html", context)



def recetasDetalle(request, id):

   all_recetas = Recetas.objects.get(id=id)
   context = {
       "recetas": all_recetas,
   }
   return render(request, "AppKaliz/recetasDetalle.html", context=context)

@login_required(login_url='accountRegister')
def busqueda_receta(request):
    # mostrar datos filtrados
    mi_formulario = BusquedaRecetasForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        recetas_filtradas = Recetas.objects.filter(Receta__icontains=informacion['Receta'])
        context = {
            "recetas": recetas_filtradas
        }
    return render(request, "AppKaliz/busqueda_receta.html", context=context)



def recetasDulces(request):

    if request.method == "POST":
        mi_formulario = RecetasDulcesForm(request.POST, request.FILES)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            receta_save = RecetasDulces(

                Receta=informacion['Receta'],
                Descripcion=informacion['Descripcion'],
                Duracion=informacion['Duracion'],
                usuario=informacion['usuario'],
                Pasos=informacion['Pasos'],
                Imagen=informacion['Imagen'],
                Ingredientes=informacion['Ingredientes'],

                            )
            receta_save.save()

    all_recetas = RecetasDulces.objects.all()
    context = {
        "recetas": all_recetas,
        "form": RecetasDulcesForm(),
        "form_busqueda": BusquedaRecetasDulcesForm()
    }
    return render(request, "AppKaliz/receta_dulce.html", context=context)

@login_required(login_url='accountRegister')
class CrearRecetaDulce(LoginRequiredMixin):
    @login_required(login_url='accountRegister')
    def crear_recetaDulce(request, fechaPublicacion, Duracion, usuario, Receta, Pasos,
                     Descripcion, Imagen, Ingredientes):

        save_receta = RecetasDulces(fechaPublicacion=fechaPublicacion, Duracion=Duracion, usuario=usuario,
                              Receta=Receta, Descripcion=Descripcion, Pasos=Pasos,
                              Imagen=Imagen, Ingredientes=Ingredientes )
        save_receta.save()
        context = {
            "Receta": RecetasDulces,

        }
        return render(request, HttpResponse, "AppKaliz/guardar_recetaDulce.html", context)


def recetasDulceDetalle(request, id):

   all_recetas = RecetasDulces.objects.get(id=id)
   context = {
       "recetas": all_recetas,
   }
   return render(request, "AppKaliz/recetasDulceDetalle.html", context=context)

@login_required(login_url='accountRegister')
def busqueda_recetaDulce(request):
    # mostrar datos filtrados
    mi_formulario = BusquedaRecetasDulcesForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        recetas_filtradas = RecetasDulces.objects.filter(Receta__icontains=informacion['Receta'])
        context = {
            "recetas": recetas_filtradas
        }
    return render(request,"AppKaliz/busqueda_recetaDulce.html", context=context)



def comentarios(request):
    if request.method == "POST":
        miFormulario = Comentarios(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            comentario_save = Comentario(usuario=informacion["usuario"], comentario=informacion["comentario"], fechaPublicacion=informacion["fechaPublicacion"])

            comentario_save.save()

    all_comentarios = Comentario.objects.all()
    context = {
            "Comentarios": all_comentarios,
            "form": Comentarios()
        }

    return render(request, "AppKaliz/comentarios.html", context=context)

class CrearComentario(LoginRequiredMixin):

    def crear_comentario(request, fechaPublicacion, usuario, comentario):

            save_comentario = Comentario(fechaPublicacion=fechaPublicacion, comentario=comentario, usuario=usuario)
            save_comentario.save()
            context = {
                "Comentario": comentario,
                "Usuario": usuario,
                "FechaPublicacion": fechaPublicacion,

            }
            return render(request, HttpResponse, "AppKaliz/recetasDetalle.html", context)