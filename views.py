from django.shortcuts import render_to_response
from django.template import RequestContext
from luciernaga.eventos.models import*
from luciernaga.multimedia.models import *
from luciernaga.material.models import *
import datetime


from luciernaga.multimedia.models import *

def index(request):
    fecha = datetime.datetime.now()
    temas = Tema.objects.filter(especifico=True)
    temasall = Tema.objects.all()
    videos_cant = Video.objects.all().count()
    next = datetime.datetime.today() + datetime.timedelta(1 * 365 / 12)
       
    eventos = Evento.objects.filter(fecha__month=fecha.month, fecha__year=fecha.year, fecha__gte=fecha).order_by('fecha')[:2]
    proximos = Evento.objects.filter(fecha__month=fecha.month+1, fecha__year=fecha.year).order_by('fecha')[:2]
    vacio = 0
    flag = 0    
    divuno_label = fecha
    divdos_label = datetime.date(fecha.year, fecha.month+1, fecha.day)
    if not eventos:
        fecha2 = datetime.date(fecha.year, fecha.month+2, fecha.day)
        eventos = Evento.objects.filter(fecha__month=fecha.month+1, fecha__year=fecha.year).order_by('fecha')[:2]
        proximos = Evento.objects.filter(fecha__gte=fecha2).order_by('fecha')[:2]
        divuno_label = divdos_label
        divdos_label = fecha2
    if not proximos and eventos:
        fecha2 = datetime.date(fecha.year, fecha.month+2, 1)
        proximos = Evento.objects.filter(fecha__gte=fecha2).order_by('fecha')[:2]
        flag = 1
    if not eventos:
        eventos = Evento.objects.filter(fecha__gte=fecha).order_by('fecha')[:2]
        proximos = []
        flag = 2
        vacio = 1
    if not eventos:
        vacio = 2
        eventos = Evento.objects.all().order_by('-fecha')[:2]
    try:
        index = FotoPortada.objects.get(slug='index')
    except: pass
    destacado = Video.objects.filter(publicar=True, destacado=True).order_by('?')[:1]
    try:
        intro = Informacion.objects.get(slug='intro')
    except:
        pass
    return render_to_response('index.html', RequestContext(request, locals()))


def CustomSearch(request):
    return render_to_response('search/search.html', RequestContext(request, locals()))