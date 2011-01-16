# -*- coding: UTF-8 -*-
from django import forms as forms
from luciernaga.captcha.fields import CaptchaField
from models import *

class SendForm(forms.Form):
    su_email = forms.EmailField()
    email_amigo = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)
    #captcha = CaptchaField()
    url = forms.CharField(widget=forms.HiddenInput())
    centinel = forms.CharField(widget=forms.HiddenInput())
    id = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        pass

class InfoForm(forms.Form):
    nombre = forms.CharField(max_length=300)
    su_email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)
    #captcha = CaptchaField()
    evento = forms.CharField(widget=forms.HiddenInput())
    id = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        pass