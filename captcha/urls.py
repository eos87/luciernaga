from django.conf.urls.defaults import *

urlpatterns = patterns('captcha.views',
    (r'image/(?P<key>\w+)/$','captcha_image'),
    url(r'audio/(?P<key>\w+)/$','captcha_audio'),
)