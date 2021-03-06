from django.conf.urls.defaults import *

urlpatterns = patterns('luciernaga.red.views',
    (r'^red/$', 'index'),
    (r'^red/(?P<id>\d+)/$', 'contenido'),
    (r'^red/perfiles/$', 'perfiles'),
    (r'^red/perfiles/(?P<username>\w+)/$', 'perfil_detail'),
)