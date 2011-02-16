from django.contrib import admin
from models import *

class ModelOptions(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("/files/css/textarea.css",)
        }

        js = ('/files/js/tiny_mce/tiny_mce.js',
              '/files/js/tiny_mce/tconfig.js')

class VideoAdmin(admin.ModelAdmin):
    list_display = ['get_portada', 'nombre', 'codigo', 'owner','user', 'anio', 'publicar', 'destacado', 'duracion', 'archivo']    
    list_filter = ['publicar', 'owner']
    search_fields = ['nombre', 'sinopsis', 'realizacion__nombre', 'produccion', 'anio', 'codigo']
    save_on_top = True
    actions_on_top = True
    fieldsets = [
        (None, {'fields': [('publicar', 'destacado')]}),
        ('Requeridos', {'fields': ['codigo', 'nombre', 'portada', 'archivo', 'owner', 'user']}),
        ('Otros Datos', {'fields': ['sinopsis', 'produccion', 'anio', 'duracion', 'color', 'elenco', 'creditos', 'derechos_autor',
         'comentarios', 'stand', 'fila', 'genero', 'coleccion', 'realizacion', 'pais_produccion', 'paises_referidos',
         'formato_original', 'formatos_distribucion', 'idioma', 'tema', 'subtema']})
    ]
        
    class Media:
        css = {
            "all": ("/files/css/vareas.css", "/files/css/requerido.css")
        }

        js = ('/files/js/tiny_mce/tiny_mce.js',
              '/files/js/tiny_mce/vconfig.js')

    def queryset(self, request):
        if request.user.is_superuser:
            return Video.objects.all()
        return Video.objects.filter(user=request.user)

    def get_form(self, request, obj=None, ** kwargs):
        if request.user.is_superuser:
            form = super(VideoAdmin, self).get_form(self, request, ** kwargs)
        else:
            form = super(VideoAdmin, self).get_form(self, request, ** kwargs)
            form.base_fields['user'].queryset = User.objects.filter(pk=request.user.pk)
            form.base_fields['owner'].choices = (('red', 'Red Mesoamericana'),)
        return form


class SubtemaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tema']
    list_filter = ['tema']
    search_fields = ['nombre', 'tema__nombre', 'descripcion']

class DirectorAdmin(admin.ModelAdmin):
    search_fields = ['nombre', ]
    save_on_top = True
    actions_on_top = True

admin.site.register(Informacion, ModelOptions)
admin.site.register(Tema, ModelOptions)
admin.site.register(Subtema, SubtemaAdmin)
admin.site.register(Genero)
admin.site.register(Coleccion)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Idioma)
admin.site.register(Pais)
admin.site.register(Formato)
admin.site.register(Video, VideoAdmin)
#admin.site.register(Huerfana)