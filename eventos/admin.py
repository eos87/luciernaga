from django.contrib import admin
from django.contrib.contenttypes import generic
from luciernaga.material.models import *
from models import *

class GenericImageInline(generic.GenericTabularInline):
    model = GenericImage
    extra = 3
    verbose_name = 'foto'
    verbose_name_plural = 'Fotos'

class GenericVideoInline(generic.GenericStackedInline):
    model = GenericVideo
    max_num = 2
    verbose_name = 'Video'
    verbose_name_plural = 'Videos'

class ModelOptions(admin.ModelAdmin):
    filter_horizontal = ['documentos']
    inlines = [
        GenericImageInline,
        GenericVideoInline
    ]
    search_fields = ['titulo', 'contenido']
    list_filter = ['fecha']
    list_display = ['titulo', 'fecha',]
    save_on_top = True
    actions_on_top = True

    class Media:
        css = {
            "all": ("/files/css/textarea.css",)
        }

        js = ('/files/js/tiny_mce/tiny_mce.js',
              '/files/js/tiny_mce/tconfig.js')


class EventoAdmin(ModelOptions):
    fieldsets = [
        (None, {'fields': ['titulo', 'portada', 'fecha', 'hora', 'direccion', 'contenido', 'documentos']}),
        ('Galeria de fotos', {'fields': ['titulo_galeria', 'fecha_galeria']}),
    ]

class NoticiaAdmin(ModelOptions):
    fieldsets = [
        (None, {'fields': ['titulo', 'portada', 'fecha', 'contenido', 'documentos']}),
        ('Galeria de fotos', {'fields': ['titulo_galeria', 'fecha_galeria']}),
    ]

admin.site.register(Evento, EventoAdmin)
admin.site.register(Noticia, NoticiaAdmin)