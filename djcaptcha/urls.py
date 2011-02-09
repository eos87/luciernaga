from django.conf.urls.defaults import *

urlpatterns = patterns('luciernaga.djcaptcha.views',
    (r'^(?P<key>\w+)/$', 'captcha'),
)


