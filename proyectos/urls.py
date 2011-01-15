from django.conf.urls.defaults import *

urlpatterns = patterns('luciernaga.proyectos.views',
    (r'^proyectos/$', 'proyectos'),
    (r'^proyectos/(?P<slug>[-\w]+)/$', 'proyecto_detail'),
    (r'^campanias/$', 'campanias'),
    (r'^campanias/(?P<slug>[-\w]+)/$', 'campania_detail'),
)