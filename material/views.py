from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from luciernaga.multimedia.models import *
from models import *

def index(request, slug):
    flag = 'material'
    temas = Tema.objects.filter(especifico=True)
    temasall = Tema.objects.all()
    tema = get_object_or_404(Tema, slug=slug)

    return render_to_response('material/index.html', RequestContext(request, locals()))
