from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from luciernaga.multimedia.models import *
from models import *

def index(request):
    flag = 'red'
    temas = Tema.objects.filter(especifico=True)
    temasall = Tema.objects.all()
    menu = Contenido.objects.all().exclude(pk=1)
    producciones = Video.objects.filter(owner='red').order_by('?')
    try:
        contenido = Contenido.objects.get(pk=1)
    except:
        pass
    return render_to_response('red/red.html', RequestContext(request, locals()))

def contenido(request, id):
    flag = 'red'
    temas = Tema.objects.filter(especifico=True)
    temasall = Tema.objects.all()
    menu = Contenido.objects.all()
    producciones = Video.objects.filter(owner='red').order_by('?')
    contenido = Contenido.objects.get(pk=id)
    return render_to_response('red/red.html', RequestContext(request, locals()))

def perfiles(request):
    temas = Tema.objects.filter(especifico=True)
    temasall = Tema.objects.all()
    menu = Contenido.objects.all()
    nicaragua = Pais.objects.get(nombre='Nicaragua')
    otros_paises = Pais.objects.all().exclude(pk=nicaragua.pk)
    return render_to_response('red/perfiles.html', RequestContext(request, locals()))

def perfil_detail(request, username):
    centinel = True
    menu = Contenido.objects.all()
    nicaragua = Pais.objects.get(nombre='Nicaragua')
    otros_paises = Pais.objects.all().exclude(pk=nicaragua.pk)
    miembro = get_object_or_404(Perfil, user__username=username)
    return render_to_response('red/perfiles.html', RequestContext(request, locals()))
