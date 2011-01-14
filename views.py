from django.shortcuts import render_to_response
from django.template import RequestContext

from luciernaga.multimedia.models import *

def index(request):
    temas = Tema.objects.filter(especifico=True)
    temasall = Tema.objects.all()
    videos_cant = Video.objects.all().count()
    try:
        intro = Informacion.objects.get(slug='intro')
    except:
        pass
    return render_to_response('index.html', RequestContext(request, locals()))

