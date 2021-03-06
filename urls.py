from django.conf.urls.defaults import *
from django.contrib import admin
from luciernaga.settings import *
import os

admin.autodiscover()
PROJECT_DIR = os.path.dirname(__file__)

urlpatterns = patterns('',    
    (r'^admin/filebrowser/', 'luciernaga.multimedia.views.subir_huerfana'),    
    
    (r'^$', 'luciernaga.views.index'),
    (r'^busqueda/$', 'luciernaga.views.CustomSearch'),
    (r'^captcha/', include('luciernaga.djcaptcha.urls')),
    (r'^', include('luciernaga.multimedia.urls')),
    (r'^', include('luciernaga.red.urls')),
    (r'^', include('luciernaga.material.urls')),
    (r'^', include('luciernaga.proyectos.urls')),
    (r'^', include('luciernaga.eventos.urls')),
    (r'^', include('luciernaga.contact.urls')),
    #(r'^busqueda/', include('haystack.urls')),


    (r'^admin/', include(admin.site.urls)),
    #(r'^captcha/image/(?P<key>\w+)/$', 'luciernaga.captcha.views.captcha_image'),
)

if DEBUG:
    urlpatterns += patterns('',
                            (r'^files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': PROJECT_DIR + '/files'}),
                            (r'^public/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
                           )
