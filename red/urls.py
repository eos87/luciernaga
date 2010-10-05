from django.conf.urls.defaults import *

urlpatterns = patterns('luciernaga.red.views',
    (r'^red/$', 'index'),
    (r'^red/(?P<id>\d+)/$', 'contenido'),
    (r'^red/perfiles/$', 'perfiles'),
    #(r'^videoteca/buscar/$', 'buscar'),
    #(r'^videoteca/(?P<slug>[-\w]+)/$', 'tema_selecto'),
    #
    #(r'^indicadores/$', 'indicadores'),
    #(r'^indicadores/(?P<vista>[-\w]+)/$', '_get_view'),
)