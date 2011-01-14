from django.conf.urls.defaults import *

urlpatterns = patterns('luciernaga.proyectos.views',
    (r'^proyectos/$', 'proyectos'),
    (r'^proyectos/(?P<slug>[-\w]+)/$', 'proyecto_detail'),
)