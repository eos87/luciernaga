from django.conf.urls.defaults import *

urlpatterns = patterns('luciernaga.material.views',
    (r'^material/(?P<slug>[-\w]+)/$', 'index'),
)


