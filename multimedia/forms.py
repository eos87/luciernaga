# -*- coding: UTF-8 -*-

from django import forms as forms
from models import *

class SearchForm(forms.Form):
    q = forms.CharField(max_length=40, label='Palabras claves')
    tema = forms.ModelMultipleChoiceField(queryset=Tema.objects.all(), widget=forms.CheckboxSelectMultiple, label="Limitar búsqueda a")

    class Meta:
        pass
        #widgets = {'temas': forms.CheckboxSelectMultiple}


