from django.contrib import admin
from luciernaga.multimedia.models import Video
from models import *

class DocumentoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha', 'user']
    #list_editable = ['user']
    search_fields = ['titulo', 'descripcion']
    save_on_top = True
    actions_on_top = True
    filter_horizontal = ('videos_relacionados',)
    fields = ['user', 'titulo', 'portada', 'descripcion', 'fecha', 'archivo', 'tema', 'videos_relacionados']

    def queryset(self, request):
        if request.user.is_superuser:
            return Documento.objects.all()
        return Documento.objects.filter(user=request.user)

    def get_form(self, request, obj=None, ** kwargs):
        if request.user.is_superuser:
            form = super(DocumentoAdmin, self).get_form(self, request, ** kwargs)
            form.base_fields['videos_relacionados'].queryset = Video.objects.filter(publicar=True)
        else:
            form = super(DocumentoAdmin, self).get_form(self, request, ** kwargs)
            form.base_fields['videos_relacionados'].queryset = Video.objects.filter(publicar=True)
            form.base_fields['user'].queryset = User.objects.filter(pk=request.user.pk)
        return form

    class Media:
        css = {
            "all": ("/files/css/vareas.css", )
        }

        js = ('/files/js/tiny_mce/tiny_mce.js',
              '/files/js/tiny_mce/vconfig.js')


admin.site.register(Documento, DocumentoAdmin)
admin.site.register(FotoPortada)


