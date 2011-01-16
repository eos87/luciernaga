from django.shortcuts import render_to_response
from django.template import RequestContext
from luciernaga.eventos.models import*
import datetime


from luciernaga.multimedia.models import *

def index(request):
    temas = Tema.objects.filter(especifico=True)
    temasall = Tema.objects.all()
    videos_cant = Video.objects.all().count()
    next = datetime.datetime.today() + datetime.timedelta(1 * 365 / 12)

    last_two = Evento.objects.all()[:2]
    try:
        intro = Informacion.objects.get(slug='intro')
    except:
        pass
    return render_to_response('index.html', RequestContext(request, locals()))

