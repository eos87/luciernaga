from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Q
from forms import *
from models import *
import operator

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
    selecto = get_object_or_404(Tema, slug=slug)    
    form = SelectoForm()    

    query = request.GET.get('q', '')
    subtema = request.GET.get('subtema', '')
    qset = []
    videos = Video.objects.filter(tema=selecto)
    if query:
        qset.append(Q(nombre__icontains=query))
        qset.append(Q(sinopsis__icontains=query))
        qset.append(Q(anio__icontains=query))
        qs = reduce(operator.or_, qset)
        resultados = videos.filter(qs).distinct()
        form = SelectoForm(request.GET)
    if subtema:        
        resultados = videos.filter(qs, subtema__pk=subtema).distinct()
        form = SelectoForm(request.GET)

    if not query and not subtema:
        resultados = Video.objects.filter(tema=selecto)

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

