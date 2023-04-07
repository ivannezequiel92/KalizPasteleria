from django.contrib import admin

from AppKaliz.models import Recetas, RecetasDulces, Comentario

# Register your models here.
admin.site.register(RecetasDulces)
admin.site.register(Recetas)
admin.site.register(Comentario)