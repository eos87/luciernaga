from django.contrib import admin
from luciernaga.multimedia.models import Video
from models import *

class ModelOptions(admin.ModelAdmin):
    filter_horizontal = ['videos', 'documentos']
    class Media:
        css = {
            "all": ("/files/css/textarea.css", )
        }

        js = ('/files/js/tiny_mce/tiny_mce.js',
              '/files/js/tiny_mce/tconfig.js')

    def get_form(self, request, obj=None, ** kwargs):
        form = super(ModelOptions, self).get_form(self, request, ** kwargs)
        form.base_fields['videos'].queryset = Video.objects.filter(publicar=True)
        return form

admin.site.register(Proyecto, ModelOptions)
admin.site.register(Campania, ModelOptions)