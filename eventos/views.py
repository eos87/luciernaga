# -*- coding: UTF-8 -*-
import calendar
import datetime
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from forms import *
from luciernaga.multimedia.models import *
from models import *
"""from luciernaga.settings import RECAPTCHA_PRIVATE_KEY
from luciernaga.settings import RECAPTCHA_PUB_KEY"""

w1, w2, w3, w4, w5 = [], [], [], [], []
fecha = datetime.datetime.today()

def eventos(request, year=fecha.year, month=fecha.month, day=None):
    f1 = []
    if day != None:
        fecha = datetime.date(int(year), int(month), int(day))
    else:
        fecha = datetime.date(int(year), int(month), datetime.date.today().day)
        
    prev = fecha - datetime.timedelta(1 * 365 / 12)
    next = fecha + datetime.timedelta(1 * 365 / 12)
    myCal = calendar.Calendar(calendar.SUNDAY)
    a = myCal.monthdayscalendar(fecha.year, fecha.month)
    w1, w2, w3, w4, w5 = calendario(a)

    flag = 'evento'
    temas = Tema.objects.filter(especifico=True)
    temasall = Tema.objects.all()
    
    if day != None:
        eventos = Evento.objects.filter(fecha__month=fecha.month, fecha__year=fecha.year, fecha__day=day)
        f1.append(int(day))
    else:
        eventos = Evento.objects.filter(fecha__month=fecha.month, fecha__year=fecha.year)

    for acts in eventos:
        f1.append(acts.fecha.day)

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
    fecha = datetime.datetime.today()
    f1 = []
    prev = fecha - datetime.timedelta(1 * 365 / 12)
    next = fecha + datetime.timedelta(1 * 365 / 12)
    myCal = calendar.Calendar(calendar.SUNDAY)
    a = myCal.monthdayscalendar(fecha.year, fecha.month)
    w1, w2, w3, w4, w5 = calendario(a)      
    eventos = Evento.objects.filter(fecha__month=fecha.month, fecha__year=fecha.year)

    for acts in eventos:
        f1.append(acts.fecha.day)

    flag = 'evento'
    temas = Tema.objects.filter(especifico=True)
    temasall = Tema.objects.all()
    evento = get_object_or_404(Evento, slug=slug)

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

    return render_to_response('eventos/evento_detail.html', RequestContext(request, locals()))

def noticias(request):
    flag = 'noticia'
    temas = Tema.objects.filter(especifico=True)
    temasall = Tema.objects.all()
    noticias = Noticia.objects.all()

    if request.method == 'POST':
        try:
            centinel = request.POST['centinel']
            form = SendForm(request.POST)
            form2 = InfoForm()
            id = request.POST['id']
            if form.is_valid():
                contenido = render_to_string('eventos/send_to_friend_1.txt', {'url': form.cleaned_data['url'], 'mensaje': form.cleaned_data['mensaje'], 'su_email': form.cleaned_data['su_email']})
                send_mail('Eventos Fundación Luciérnaga', contenido, 'noreply@fundacionluciernaga.org', [form.cleaned_data['email_amigo']])
                return HttpResponseRedirect(form.cleaned_data['url'])
        except:
            form = SendForm()
            form2 = InfoForm(request.POST)
            id = request.POST['id']
            if form2.is_valid():
                contenido = render_to_string('eventos/request_info_1.txt', {'evento': form2.cleaned_data['evento'], 'mensaje': form2.cleaned_data['mensaje'], 'su_email': form2.cleaned_data['su_email']})
                send_mail('Eventos Fundación Luciérnaga', contenido, form2.cleaned_data['su_email'], ['eventos@fundacionluciernaga.org'])
                return HttpResponseRedirect('http://fundacionluciernaga.org/noticias/')
    else:
        form = SendForm()
        form2 = InfoForm()

    return render_to_response('eventos/noticias_list.html', RequestContext(request, locals()))


def noticia_detail(request, slug):
    flag = 'noticia'
    temas = Tema.objects.filter(especifico=True)
    temasall = Tema.objects.all()
    evento = get_object_or_404(Noticia, slug=slug)
    cinco = Noticia.objects.all().exclude(pk=evento.pk)[:5]

    return render_to_response('eventos/noticia_detail.html', RequestContext(request, locals()))

#Calendario de eventos
def calendario(a):
    contador = 0
    semana = 1
    w1, w2, w3, w4, w5 = [], [], [], [], []
    for i in a:
        for j in i:
            if semana == 1 and contador < 7:
                contador += 1
                if j == 0:
                    j = ""
                w1.append(j)
                if contador == 7:
                    semana = 2
                    contador = 0
                    break
            if semana == 2 and contador < 7:
                contador += 1
                w2.append(j)
                if contador == 7:
                    semana = 3
                    contador = 0
                    break
            if semana == 3 and contador < 7:
                contador += 1
                w3.append(j)
                if contador == 7:
                    semana = 4
                    contador = 0
                    break
            if semana == 4 and contador < 7:
                contador += 1
                w4.append(j)
                if contador == 7:
                    semana = 5
                    contador = 0
                    break
            if semana == 5 and contador < 7:
                contador += 1
                if j == 0:
                    j = ""
                w5.append(j)

    return w1, w2, w3, w4, w5