from django.shortcuts import render_to_response
from django.template import RequestContext
from luciernaga.eventos.models import*
from luciernaga.multimedia.models import *
from luciernaga.material.models import *
import datetime


from luciernaga.multimedia.models import *

def index(request):
    y = request.GET.get('y', '')
    m = request.GET.get('m', '')
    temas = Tema.objects.filter(especifico=True)
    temasall = Tema.objects.all()
    videos_cant = Video.objects.all().count()
    next = datetime.datetime.today() + datetime.timedelta(1 * 365 / 12)
    c = True   
    last_two = Evento.objects.all()[:2]
    try:
        index = FotoPortada.objects.get(slug='index')
    except: pass
    destacado = Video.objects.filter(publicar=True, destacado=True).order_by('?')[:1]
    try:
        intro = Informacion.objects.get(slug='intro')
    except:
        pass
    return render_to_response('index.html', RequestContext(request, locals()))

from haystack.query import SearchQuerySet

def CustomSearch(request):    

    return render_to_response('search/search.html', RequestContext(request, locals()))