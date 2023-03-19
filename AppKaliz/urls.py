
from django.urls import path
from AppKaliz.views import inicio, clientes, alfajores, crear_alfajor, tortas

urlpatterns = [

    path('inicio', inicio, name="AppKalizInicio"),
    path('clientes/', clientes, name="AppKalizClientes"),
    path('alfajores/', alfajores, name="AppKalizAlfajores"),
    path('alfajor/<nombre>/<tipo>/<sabor>', crear_alfajor, name="AppKalizCrearAlfajor"),
    path('tortas/', tortas, name="AppKalizTortas"),
]
