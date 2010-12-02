from django.contrib import admin
from models import *

class ModelOptions(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("/files/css/textarea.css", )
        }

        js = ('/files/js/tiny_mce/tiny_mce.js',
              '/files/js/tiny_mce/tconfig.js')

admin.site.register(Informacion, ModelOptions)
admin.site.register(Tema, ModelOptions)
admin.site.register(Subtema)
admin.site.register(Genero)
admin.site.register(Coleccion)
admin.site.register(Video)


