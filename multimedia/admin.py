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
    list_display = ['get_portada', 'nombre', 'codigo', 'owner', 'anio', 'publicar', 'duracion']
    search_fields = ['nombre', 'sinopsis', 'realizacion__nombre', 'produccion', 'anio', 'codigo']
    save_on_top = True
    actions_on_top = True
    
    class Media:
        css = {
            "all": ("/files/css/vareas.css", )
        }

        js = ('/files/js/tiny_mce/tiny_mce.js',
              '/files/js/tiny_mce/vconfig.js')


class SubtemaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tema']
    list_filter = ['tema']

admin.site.register(Informacion, ModelOptions)
admin.site.register(Tema, ModelOptions)
admin.site.register(Subtema, SubtemaAdmin)
admin.site.register(Genero)
admin.site.register(Coleccion)
admin.site.register(Director)
admin.site.register(Idioma)
admin.site.register(Pais)
admin.site.register(Formato)
admin.site.register(Video, VideoAdmin)