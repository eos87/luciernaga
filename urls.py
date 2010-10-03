from django.conf.urls.defaults import *
from django.contrib import admin
import os

admin.autodiscover()
PROJECT_DIR = os.path.dirname(__file__)

urlpatterns = patterns('',
    (r'^files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': PROJECT_DIR + '/files'}),
    (r'^$', 'luciernaga.views.index'),
    (r'^', include('multimedia.urls')),
    (r'^admin/', include(admin.site.urls)),
)
