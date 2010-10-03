from django.views.generic.simple import direct_to_template
from django.shortcuts import render_to_response
from django.template import RequestContext

from multimedia.models import *

def index(request):
    temas = Tema.objects.filter(especifico=True)
    temasall = Tema.objects.all()
    return render_to_response('index.html', RequestContext(request, locals()))


