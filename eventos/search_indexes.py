# -*- coding: UTF-8 -*-
from haystack.indexes import *
from haystack import site
from models import *
import datetime

class EventoIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    titulo = CharField(model_attr='titulo')
    fecha = DateField(model_attr='fecha')

    def get_queryset(self):
        return Evento.objects.filter(fecha__lte=datetime.datetime.now())

site.register(Evento, EventoIndex)

class NoticiaIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    titulo = CharField(model_attr='titulo')
    fecha = DateField(model_attr='fecha')

    def get_queryset(self):
        return Noticia.objects.filter(fecha__lte=datetime.datetime.now())

site.register(Noticia, NoticiaIndex)


