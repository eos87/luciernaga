from django.shortcuts import render_to_response
from django.template import RequestContext

from models import *

def buscar(request):
    temas = Tema.objects.filter(especifico=True)
    temasall = Tema.objects.all()
    return render_to_response('videoteca.html', RequestContext(request, locals()))

def tema_selecto(request, slug):
    temas = Tema.objects.filter(especifico=True)
    temasall = Tema.objects.all().exclude(slug=slug)
    return render_to_response('videoteca.html', RequestContext(request, locals()))

