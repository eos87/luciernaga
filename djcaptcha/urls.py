from django.conf.urls.defaults import *

urlpatterns = patterns('djcaptcha.views',
    (r'^(?P<key>\w+)/$', 'captcha'),
)


