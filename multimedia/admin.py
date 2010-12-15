from django.contrib import admin
from models import *

class ModelOptions(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("/files/css/textarea.css", )
        }

        js = ('/files/js/tiny_mce/tiny_mce.js',
              '/files/js/tiny_mce/tconfig.js')

class VideoAdmin(admin.ModelAdmin):
    list_display = ['get_portada', 'nombre', 'owner', 'anio']
    search_fields = ['nombre', 'sinopsis', 'realizacion', 'produccion', 'anio']
    
    class Media:
        css = {
            "all": ("/files/css/vareas.css", )
        }

        js = ('/files/js/tiny_mce/tiny_mce.js',
              '/files/js/tiny_mce/vconfig.js')


admin.site.register(Informacion, ModelOptions)
admin.site.register(Tema, ModelOptions)
admin.site.register(Subtema)
admin.site.register(Genero)
admin.site.register(Coleccion)
admin.site.register(Video, VideoAdmin)


