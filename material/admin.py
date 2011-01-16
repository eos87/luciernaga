from django.contrib import admin
from luciernaga.multimedia.models import Video
from models import *

class DocumentoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha']
    search_fields = ['titulo', 'descripcion']
    save_on_top = True
    actions_on_top = True
    filter_horizontal = ('videos_relacionados',)

    def get_form(self, request, obj=None, ** kwargs):
        form = super(DocumentoAdmin, self).get_form(self, request, ** kwargs)
        form.base_fields['videos_relacionados'].queryset = Video.objects.filter(publicar=True)
        return form

    class Media:
        css = {
            "all": ("/files/css/vareas.css", )
        }

        js = ('/files/js/tiny_mce/tiny_mce.js',
              '/files/js/tiny_mce/vconfig.js')


admin.site.register(Documento, DocumentoAdmin)
admin.site.register(FotoPortada)


