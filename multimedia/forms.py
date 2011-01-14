# -*- coding: UTF-8 -*-

from django import forms as forms
from models import *

class SearchForm(forms.Form):
    q = forms.CharField(max_length=40, label='Palabras claves')
    tema = forms.ModelMultipleChoiceField(queryset=Tema.objects.all(), widget=forms.CheckboxSelectMultiple, label='Limitar búsqueda a')

    class Meta:
        pass
        #widgets = {'temas': forms.CheckboxSelectMultiple}

class VideoBuscar(forms.Form):
    tema = forms.ModelChoiceField(queryset=Tema.objects.all(), empty_label='Tema')
    genero = forms.ModelChoiceField(queryset=Genero.objects.all(), empty_label='Género')
    coleccion = forms.ModelChoiceField(queryset=Coleccion.objects.all(), empty_label='Colección')

    class Meta:
        pass

class SelectoForm(forms.Form):
    def __init__(self, selecto, *args, **kwargs):
        super(SelectoForm, self).__init__(*args, **kwargs)
        self.fields['subtema'] = forms.ModelChoiceField(queryset=Subtema.objects.filter(tema=selecto), label="Subtema", empty_label='Todos')
        self.fields['q'] = forms.CharField(max_length=40, label='Palabras claves')
        
    class Meta:
        pass
class HuerfanaForm(forms.ModelForm):
    class Meta:
        model = Huerfana
