# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from luciernaga.multimedia.models import *
from models import *

def proyectos(request):
    flag = 'proyecto'
    temas = Tema.objects.filter(especifico=True)
    temasall = Tema.objects.all()
    try:
        info = Informacion.objects.get(slug='proyectos')
    except:
        pass

    proyectos = Proyecto.objects.all()
    return render_to_response('proyectos/proyectos.html', RequestContext(request, locals()))

def proyecto_detail(request, slug):
    flag = 'proyecto'
    temas = Tema.objects.filter(especifico=True)
    temasall = Tema.objects.all()
    proyecto = get_object_or_404(Proyecto, slug=slug)

    return render_to_response('proyectos/proyecto_detail.html', RequestContext(request, locals()))

def campanias(request):
    flag = 'proyecto'
    temas = Tema.objects.filter(especifico=True)
    temasall = Tema.objects.all()
    try:
        info = Informacion.objects.get(slug='campanias')
    except:
        pass

    proyectos = Campania.objects.all()
    return render_to_response('proyectos/campanias.html', RequestContext(request, locals()))

def campania_detail(request, slug):
    flag = 'proyecto'
    temas = Tema.objects.filter(especifico=True)
    temasall = Tema.objects.all()
    proyecto = get_object_or_404(Campania, slug=slug)

    return render_to_response('proyectos/campania_detail.html', RequestContext(request, locals()))

