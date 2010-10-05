from django.shortcuts import render_to_response
from django.template import RequestContext
from luciernaga.multimedia.models import *
from models import *

def index(request):
    temas = Tema.objects.filter(especifico=True)
    menu = Contenido.objects.all()
    contenido = Contenido.objects.get(pk=1)
    return render_to_response('red/red.html', RequestContext(request, locals()))

def contenido(request, id):
    temas = Tema.objects.filter(especifico=True)
    menu = Contenido.objects.all()
    contenido = Contenido.objects.get(pk=id)
    return render_to_response('red/red.html', RequestContext(request, locals()))

def perfiles(request):
    temas = Tema.objects.filter(especifico=True)
    menu = Contenido.objects.all()
    contenido = Contenido.objects.get(nombre='perfil')
    return render_to_response('red/red.html', RequestContext(request, locals()))
