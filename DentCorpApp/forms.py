from DentCorpApp.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Especialidades

class EspecialidadesForm(forms.ModelForm):
    class Meta:
        model = Especialidades
        fields = ['nombre_espec']
