from django.conf.urls.defaults import *

urlpatterns = patterns('luciernaga.multimedia.views',
    (r'^videoteca/$', 'buscar'),
    (r'^videoteca/buscar/$', 'buscar'),
    (r'^videoteca/(?P<slug>[-\w]+)/$', 'tema_selecto'),
    (r'^videoteca/video/(?P<id>\d+)/$', 'video_selecto'),
    #(r'^indicadores/$', 'indicadores'),
    #(r'^indicadores/(?P<vista>[-\w]+)/$', '_get_view'),
)


