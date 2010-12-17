from django.contrib import admin
from models import *


class ModelOptions(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("/files/css/textarea.css", )
        }

        js = ('/files/js/tiny_mce/tiny_mce.js',
              '/files/js/tiny_mce/tconfig.js')

admin.site.register(Director)
admin.site.register(Idioma)
admin.site.register(Formato)
admin.site.register(Pais)
admin.site.register(Perfil)
admin.site.register(Contenido, ModelOptions)
admin.site.register(Documentos)




