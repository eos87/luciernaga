import operator

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
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
    qset = []
    if request.method == 'POST':
        form = SearchForm(request.POST)        
        query = request.POST['q']
        themes = None
        try:
            themes = request.POST.copy().pop('tema')
            videos = Video.objects.filter(tema__pk__in=themes)
        except:
            pass

        if query:
            qset.append(Q(nombre__icontains=query))
            qset.append(Q(sinopsis__icontains=query))
            qset.append(Q(anio__icontains=query))
            qs = reduce(operator.or_, qset)
            try:
                resultados = videos.filter(qs).distinct()
            except:
                resultados = Video.objects.filter(qs).distinct()
    else:
        form = SearchForm()
    
        
    return render_to_response('busqueda.html', RequestContext(request, locals()))

def tema_selecto(request, slug):
    flag = 'videoteca'
    #objetos por pagina
    opp = 15
    temas = Tema.objects.filter(especifico=True)
    temasall = Tema.objects.all().exclude(slug=slug)    
    selecto = get_object_or_404(Tema, slug=slug)    
    form = SelectoForm(selecto)

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
        form = SelectoForm(selecto, request.GET)
    if subtema and not query:
        resultados = videos.filter(subtema__pk=subtema).distinct()
        form = SelectoForm(selecto, request.GET)

    if subtema and query:
        resultados = videos.filter(qs, subtema__pk=subtema).distinct()
        form = SelectoForm(selecto, request.GET)

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

def get_subtema(request, id):
    results = []
    subtemas = Subtema.objects.filter(tema__pk=id).values('id', 'nombre')
    dicc = {
        'subtemas': list(subtemas)
    }
    results.append(dicc)
    
    return HttpResponse(simplejson.dumps(list(subtemas)), mimetype='application/json')
