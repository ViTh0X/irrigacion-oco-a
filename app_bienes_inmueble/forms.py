from django import forms
from .models import *


class HuertoFormulario(forms.ModelForm):
    class Meta:
        model = Inmuebles
        fields = ['nombre']