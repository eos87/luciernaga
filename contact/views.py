# -*- coding: UTF-8 -*-
from django.core.mail import send_mail
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from forms import ContactForm
from luciernaga.multimedia.models import Informacion

def index(request):
    try:
        info = Informacion.objects.get(slug='contact')
    except:
        pass
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contenido = render_to_string('contact/contact.txt', {'nombre': form.cleaned_data['nombre'], 'email': form.cleaned_data['email'], 'mensaje': form.cleaned_data['mensaje']})
            send_mail(u'Contáctenos @ Fundación Luciernaga', contenido, 'noreply@fundacionluciernaga.org', ['joaquin@fundacionluciernaga.org', ])
            ok = True
    else:
        form = ContactForm()
    return render_to_response('contact/index.html', RequestContext(request, locals()))
