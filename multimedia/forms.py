# -*- coding: UTF-8 -*-

from django import forms as forms
from models import *

class SearchForm(forms.Form):
    q = forms.CharField(max_length=40, label='Palabras claves')
    tema = forms.ModelMultipleChoiceField(queryset=Tema.objects.all(), widget=forms.CheckboxSelectMultiple, label="Limitar búsqueda a")

    class Meta:
        pass
        #widgets = {'temas': forms.CheckboxSelectMultiple}

class VideoBuscar(forms.Form):
    tema = forms.ModelChoiceField(queryset=Tema.objects.all(), empty_label='Tema')
    genero = forms.ModelChoiceField(queryset=Genero.objects.all(), empty_label='Subtema')
    coleccion = forms.ModelChoiceField(queryset=Coleccion.objects.all(), empty_label='Colección')

    class Meta:
        pass

class SelectoForm(forms.Form):
    q = forms.CharField(max_length=40, label='Palabras claves')
    subtema = forms.ModelChoiceField(queryset=Tema.objects.all(), label="Subtema", empty_label='Todos')

    class Meta:
        pass