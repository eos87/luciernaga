# -*- coding: UTF-8 -*-
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
    menu = Informacion.objects.all().exclude(slug=slug)
    return render_to_response('info.html', RequestContext(request, locals()))

def tema_detail(request, slug):
    flag = 'temas'
    contenido = Tema.objects.get(slug=slug)
    temas = Tema.objects.filter(especifico=True).exclude(pk=contenido.pk)
    temasall = Tema.objects.all()
    return render_to_response('tema.html', RequestContext(request, locals()))

def buscar(request):
    flag = 'videoteca'    
    centinela = True
    temas = Tema.objects.filter(especifico=True)
    temasall = Tema.objects.all()
    qset = []
    resultados = []
    themes = []
    query = request.GET.get('q', '')
    genero = request.GET.get('genero', '')
    coleccion = request.GET.get('coleccion', '')
    try:
        themes = request.GET.copy().pop('tema')
    except:
        pass
    if query or themes:
        opp = 15
        centinela = False
        form = SearchForm(data=request.GET)
    else:
        form = SearchForm()

    #validando si selecciono algun tema
    if themes != [u'']:
        resultados = Video.objects.filter(tema__pk__in=themes, publicar=True)
    #validando si selecciono un tipo de genero
    if genero:
        resultados = Video.objects.filter(genero__pk=genero, publicar=True)
    #validando si selecciono una coleccion
    if coleccion:
        resultados = Video.objects.filter(coleccion__pk=coleccion, publicar=True)
        
    #verificar si hay palabras claves
    if query:
        qset.append(Q(nombre__icontains=query))
        qset.append(Q(sinopsis__icontains=query))
        qset.append(Q(anio__icontains=query))
        #qset.append(Q(produccion__icontains=query))
        #qset.append(Q(realizacion__icontains=query))
        qs = reduce(operator.or_, qset)
        if resultados:
            resultados = resultados.filter(qs).distinct()
        else:
            resultados = Video.objects.filter(qs, publicar=True).distinct()
        
    return render_to_response('busqueda.html', RequestContext(request, locals()))

def tema_selecto(request, slug):
    flag = 'videoteca'
    temas = Tema.objects.filter(especifico=True)
    temasall = Tema.objects.all().exclude(slug=slug)
    selecto = get_object_or_404(Tema, slug=slug)

    #objetos por pagina
    opp = 15
    order = 'subtema'
    n = request.GET.get('n', '')
    s = request.GET.get('order', '')
    if n:
        opp = int(n)
    if s:
        order = s

    #utilizado para validar si se muestrar los ordering en la plantilla
    centinela2 = True    
    form = SelectoForm(selecto)    

    query = request.GET.get('q', '')
    subtema = request.GET.get('subtema', '')
    qset = []    
    videos = Video.objects.filter(tema=selecto, publicar=True).order_by(order)
    if query:
        qset.append(Q(nombre__icontains=query))
        qset.append(Q(sinopsis__icontains=query))
        qset.append(Q(anio__icontains=query))
        #qset.append(Q(produccion__icontains=query))
        #qset.append(Q(realizacion__icontains=query))
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
        resultados = Video.objects.filter(tema=selecto, publicar=True)

    return render_to_response('videoteca.html', RequestContext(request, locals()))

def video_selecto(request, id):
    flag = 'videoteca'
    try:
        video = Video.objects.get(pk=id)
        temas = Tema.objects.filter(especifico=True)
        temasall = Tema.objects.all()
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

def subir_huerfana(request):
    if request.method == 'POST':
        form = HuerfanaForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            if 'archivo' in request.FILES:
                new = Huerfana()               	
                new.archivo = request.FILES['archivo']
                new.save()
                imagen = new
    else:
        form = HuerfanaForm()

    if request.is_ajax():
        id = request.POST['id']
        obj = Huerfana.objects.get(pk=int(id))
        obj.delete()

    return render_to_response('multimedia/subir_huerfana.html', RequestContext(request, locals()))
