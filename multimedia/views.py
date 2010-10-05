from django.shortcuts import render_to_response
from django.template import RequestContext

from forms import *
from models import *

def buscar(request):
    temas = Tema.objects.filter(especifico=True)
    temasall = Tema.objects.all()
    form = SearchForm()
    return render_to_response('videoteca.html', RequestContext(request, locals()))

def tema_selecto(request, slug):
    temas = Tema.objects.filter(especifico=True)
    temasall = Tema.objects.all().exclude(slug=slug)
    return render_to_response('videoteca.html', RequestContext(request, locals()))

def video_selecto(request, id):
    try:
        video = Video.objects.get(pk=id)
    except:
        pass
    return render_to_response('video_selecto.html', RequestContext(request, locals()))

