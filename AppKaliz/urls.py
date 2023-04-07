
from django.urls import path
from AppKaliz.views import CrearComentario, comentarios, recetasDetalle, inicio, recetas, CrearReceta, busqueda_receta, busqueda_recetaDulce, recetasDulces, recetasDulceDetalle, CrearRecetaDulce
from AppKaliz import views

urlpatterns = [

    path('inicio', inicio, name="AppKalizInicio"),
    path('buscarRecetas/', busqueda_receta, name="AppKalizBuscarReceta"),
    path('crearReceta/', CrearReceta.crear_receta, name="AppKalizCrearReceta"),
    path('recetaDetalle/<id>', recetasDetalle, name="AppKalizRecetaDetalle"),
    path('recetas/', recetas, name="AppKalizRecetas"),
    path('buscarRecetasDulces/', busqueda_recetaDulce, name="AppKalizBuscarRecetaDulce"),
    path('crearRecetaDulce/', CrearRecetaDulce.crear_recetaDulce, name="AppKalizCrearRecetaDulce"),
    path('recetaDulceDetalle/<id>', recetasDulceDetalle, name="AppKalizRecetaDulceDetalle"),
    path('recetasDulces/', recetasDulces, name="AppKalizRecetasDulces"),
    path('comentarios/', comentarios, name="Comentarios"),
    path('crearComentario/', CrearComentario.crear_comentario, name="CrearComentario"),
]
