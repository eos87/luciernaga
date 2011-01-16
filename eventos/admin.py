from django.contrib import admin
from luciernaga.multimedia.models import Video
from models import *

class ModelOptions(admin.ModelAdmin):
    filter_horizontal = ['documentos']
    class Media:
        css = {
            "all": ("/files/css/textarea.css", )
        }

        js = ('/files/js/tiny_mce/tiny_mce.js',
              '/files/js/tiny_mce/tconfig.js')

class NoticiaOptions(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("/files/css/textarea.css", )
        }

        js = ('/files/js/tiny_mce/tiny_mce.js',
              '/files/js/tiny_mce/tconfig.js')

admin.site.register(Evento, ModelOptions)
admin.site.register(Noticia, NoticiaOptions)