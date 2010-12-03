from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404

from forms import *
from models import *

def info(request, slug):
    flag = 'quien'
    contenido = Informacion.objects.get(slug=slug)
    temas = Tema.objects.filter(especifico=True)
    temasall = Tema.objects.all()
    menu = Informacion.objects.all()    
    return render_to_response('info.html', RequestContext(request, locals()))

def tema_detail(request, slug):
    flag = 'temas'
    contenido = Tema.objects.get(slug=slug)
    temas = Tema.objects.filter(especifico=True).exclude(pk=contenido.pk)
    temasall = Tema.objects.all()
    return render_to_response('tema.html', RequestContext(request, locals()))

def buscar(request):
    flag = 'videoteca'
    temas = Tema.objects.filter(especifico=True)
    temasall = Tema.objects.all()
    form = SearchForm()
    return render_to_response('busqueda.html', RequestContext(request, locals()))

def tema_selecto(request, slug):
    flag = 'videoteca'
    temas = Tema.objects.filter(especifico=True)
    temasall = Tema.objects.all().exclude(slug=slug)
    form = SelectoForm()
    selecto = get_object_or_404(Tema, slug=slug)
    return render_to_response('videoteca.html', RequestContext(request, locals()))

def video_selecto(request, id):
    flag = 'videoteca'
    try:
        video = Video.objects.get(pk=id)
        temas = Tema.objects.filter(especifico=True)
        temasall = Tema.objects.all().exclude(slug=video.tema.slug)
    except:
        pass
    return render_to_response('video_selecto.html', RequestContext(request, locals()))

