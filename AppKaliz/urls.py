
from django.urls import path
from AppKaliz.views import inicio, clientes, alfajores, crear_alfajor, tortas, busqueda_alfajor, busqueda_torta, crear_torta

urlpatterns = [

    path('inicio', inicio, name="AppKalizInicio"),
    path('clientes/', clientes, name="AppKalizClientes"),
    path('alfajores/', alfajores, name="AppKalizAlfajores"),
    path('buscarAlfajores/', busqueda_alfajor, name="AppKalizBuscarAlfajor"),
    path('alfajor/<nombre>/<tipo>/<sabor>', crear_alfajor, name="AppKalizCrearAlfajor"),
    path('tortas/', tortas, name="AppKalizTortas"),
    path('buscarTortas/', busqueda_torta, name="AppKalizBuscarTortas"),
    path('torta/<nombre>/<peso>', crear_torta, name="AppKalizCrearTorta"),
]
