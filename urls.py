from django.conf.urls.defaults import *
from django.contrib import admin
from luciernaga.settings import *
import os

admin.autodiscover()
PROJECT_DIR = os.path.dirname(__file__)

urlpatterns = patterns('',
    (r'^files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': PROJECT_DIR + '/files'}),
    (r'^public/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
    (r'^admin/filebrowser/', 'luciernaga.multimedia.views.subir_huerfana'),
    (r'^admin/', include(admin.site.urls)),
    
    (r'^$', 'luciernaga.views.index'),
    (r'^captcha/image/$', 'captcha.views.captcha_image'),
    (r'^', include('luciernaga.eventos.urls')),
    (r'^', include('luciernaga.multimedia.urls')),
    (r'^', include('luciernaga.red.urls')),
    (r'^', include('luciernaga.material.urls')),
    (r'^', include('luciernaga.proyectos.urls')),    
    
    #(r'^captcha/image/(?P<key>\w+)/$', 'luciernaga.captcha.views.captcha_image'),
)

