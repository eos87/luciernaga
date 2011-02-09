from django.forms.fields import CharField, MultiValueField
from django.forms import ValidationError
from django.forms.widgets import TextInput, MultiWidget, HiddenInput
from models import CaptchaStore
from utils import *
import datetime

CAPTCHA_OUTPUT_FORMAT = u'%(image)s %(hidden_field)s %(text_field)s'

class CaptchaTextInput(MultiWidget):
    def __init__(self,attrs=None, **kwargs):
        self._args = kwargs
        widgets = (
            HiddenInput(attrs),
            TextInput(attrs),
        )

        super(CaptchaTextInput,self).__init__(widgets,attrs)

    def decompress(self,value):
        if value:
            return value.split(',')
        return [None,None]

    def format_output(self, rendered_widgets):
        hidden_field, text_field = rendered_widgets
        return self._args.get('output_format') % dict(image=self.image, hidden_field=hidden_field, text_field=text_field)

    def render(self, name, value, attrs=None):
    
        code, respuesta = get_code()()

        store = CaptchaStore.objects.create(code=code, respuesta=respuesta)
        key = store.hashkey
        value = [key, u'']

        self.image = '<img src="/captcha/%s" alt="captcha" class="captcha" />' % key

        return super(CaptchaTextInput, self).render(name, value, attrs=attrs)

class CaptchaField(MultiValueField):

    def __init__(self, *args,**kwargs):
        fields = (
            CharField(show_hidden_initial=True),
            CharField(),
        )
        if 'error_messages' not in kwargs or 'invalid' not in kwargs.get('error_messages'):
            if 'error_messages' not in kwargs:
                kwargs['error_messages'] = dict()
            kwargs['error_messages'].update(dict(invalid='Invalid CAPTCHA'))

        widget_kwargs = dict(
            output_format = kwargs.get('output_format', None) or CAPTCHA_OUTPUT_FORMAT
        )
        for k in ('output_format',):
            if k in kwargs:
                del(kwargs[k])

        super(CaptchaField,self).__init__(fields=fields, widget=CaptchaTextInput(**widget_kwargs), *args, **kwargs)


    def compress(self,data_list):
        if data_list:
            return ','.join(data_list)
        return None

    def clean(self, value):
        super(CaptchaField, self).clean(value)
        respuesta, value[1] = value[1].strip().lower(), ''
        CaptchaStore.remove_expired()
        try:
            store = CaptchaStore.objects.get(respuesta=respuesta, hashkey=value[0], expiration__gt=datetime.datetime.now())
            store.delete()
        except Exception:
            raise ValidationError(getattr(self,'error_messages',dict()).get('invalid', 'Invalid CAPTCHA'))
        return value


