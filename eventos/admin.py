from django.contrib import admin
from django.contrib.contenttypes import generic
from luciernaga.material.models import *
from models import *

class GenericImageInline(generic.GenericTabularInline):
    model = GenericImage
    extra = 3
    verbose_name = 'foto'
    verbose_name_plural = 'Galeria de fotos'

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

    class Media:
        css = {
            "all": ("/files/css/textarea.css",)
        }

        js = ('/files/js/tiny_mce/tiny_mce.js',
              '/files/js/tiny_mce/tconfig.js')


admin.site.register(Evento, ModelOptions)
admin.site.register(Noticia, ModelOptions)