from django import forms
from django.core.exceptions import ValidationError
from DentCorpApp.models import Turnos
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


from django import forms
from .models import Turnos

class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turnos
        fields = ['fecha_hr_turno', 'autorizado', 'id_serv_odon', 'id_cob_usu', 'id_rol_usu', 'id_asig_cons']

class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=100, required=False)

# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = User
#         fields = ('email',)



class CustomUserChangeForm(UserChangeForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = (
            'email','image'
        )
        labels = {
            'email': 'Correo Electrónico',
        }