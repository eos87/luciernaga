# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from luciernaga.multimedia.models import *
from models import *

def eventos(request):
    flag = 'evento'
    temas = Tema.objects.filter(especifico=True)
    temasall = Tema.objects.all()
    eventos = Evento.objects.all()
    return render_to_response('eventos/eventos_list.html', RequestContext(request, locals()))
