from django.conf.urls.defaults import *

urlpatterns = patterns('luciernaga.captcha.views',
    url(r'image/(?P<key>\w+)/$','captcha_image'),
    #url(r'^audio/(?P<key>\w+)/$','captcha_audio',name='captcha-audio'),
)
