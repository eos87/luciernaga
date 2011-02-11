# -*- coding: UTF-8 -*-
from django import forms as forms
from luciernaga.djcaptcha.fields import CaptchaField

class ContactForm(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)
    captcha = CaptchaField()

    class Meta:
        pass


