from django.conf.urls.defaults import *

urlpatterns = patterns('luciernaga.eventos.views',
    (r'^eventos/$', 'eventos'),
    (r'^eventos/(?P<slug>[-\w]+)/$', 'evento_detail'),
    (r'^eventos/(?P<year>\d{4})/(?P<month>\w{1,2})/$', 'eventos'),
    (r'^eventos/(?P<year>\d{4})/(?P<month>\w{1,2})/(?P<day>\w{1,2})/$', 'eventos'),
    (r'^noticias/$', 'noticias'),
    (r'^noticias/(?P<slug>[-\w]+)/$', 'noticia_detail'),
)


