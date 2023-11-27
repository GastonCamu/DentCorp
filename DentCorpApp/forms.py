from django import forms
from django.core.exceptions import ValidationError
from DentCorpApp.models import Turnos

from django import forms
from .models import Turnos, User, Ciudades

class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turnos
        fields = ['fecha_hr_turno', 'autorizado', 'id_serv_odon', 'id_cob_usu', 'id_rol_usu', 'id_asig_cons']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email', 'fecha_alta_usu', 'fecha_baja_usu', 'dni_usu', 'dom_usu', 'tel_usu', 'id_ciu']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['fecha_alta_usu'].widget.attrs.update({'class': 'datepicker'})  # Añadir una clase para un datepicker, por ejemplo

class SearchForm(forms.Form):
    search_term = forms.CharField(required=False)
    filtro = forms.CharField(required=False)