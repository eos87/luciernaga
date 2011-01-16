# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from luciernaga.multimedia.models import *
from models import *
from forms import *
"""from luciernaga.settings import RECAPTCHA_PRIVATE_KEY
from luciernaga.settings import RECAPTCHA_PUB_KEY"""

def eventos(request):
    flag = 'evento'
    temas = Tema.objects.filter(especifico=True)
    temasall = Tema.objects.all()
    eventos = Evento.objects.all()
    if request.method == 'POST':
        try:
            centinel = request.POST['centinel']
            form = SendForm(request.POST)
            form2 = InfoForm()
            id = request.POST['id']
            if form.is_valid():
                contenido = render_to_string('eventos/send_to_friend.txt', {'url': form.cleaned_data['url'], 'mensaje': form.cleaned_data['mensaje'], 'su_email': form.cleaned_data['su_email']})
                send_mail('Eventos Fundación Luciérnaga', contenido, 'noreply@fundacionluciernaga.org', [form.cleaned_data['email_amigo']])
                return HttpResponseRedirect(form.cleaned_data['url'])
        except:
            form = SendForm()
            form2 = InfoForm(request.POST)
            id = request.POST['id']
            if form2.is_valid():
                contenido = render_to_string('eventos/request_info.txt', {'evento': form2.cleaned_data['evento'], 'mensaje': form2.cleaned_data['mensaje'], 'su_email': form2.cleaned_data['su_email']})
                send_mail('Eventos Fundación Luciérnaga', contenido, form2.cleaned_data['su_email'], ['eventos@fundacionluciernaga.org'])
                return HttpResponseRedirect('http://fundacionluciernaga.org/eventos/')
    else:
        form = SendForm()
        form2 = InfoForm()
    return render_to_response('eventos/eventos_list.html', RequestContext(request, locals()))


def evento_detail(request, slug):
    flag = 'evento'
    temas = Tema.objects.filter(especifico=True)
    temasall = Tema.objects.all()
    evento = get_object_or_404(Evento, slug=slug)

    return render_to_response('eventos/evento_detail.html', RequestContext(request, locals()))

def noticias(request):
    flag = 'noticia'
    temas = Tema.objects.filter(especifico=True)
    temasall = Tema.objects.all()
    noticias = Noticia.objects.all()

    return render_to_response('eventos/noticias_list.html', RequestContext(request, locals()))


def noticia_detail(request, slug):
    flag = 'evento'
    temas = Tema.objects.filter(especifico=True)
    temasall = Tema.objects.all()
    evento = get_object_or_404(Noticia, slug=slug)
    cinco = Noticia.objects.all().exclude(pk=evento.pk)[:5]

    return render_to_response('eventos/noticia_detail.html', RequestContext(request, locals()))