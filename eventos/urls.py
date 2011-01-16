from django.conf.urls.defaults import *

urlpatterns = patterns('luciernaga.eventos.views',
    (r'^eventos/$', 'eventos'),
    (r'^eventos/(?P<slug>[-\w]+)/$', 'evento_detail'),
)


