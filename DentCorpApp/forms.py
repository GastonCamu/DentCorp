from django import forms
from django.core.exceptions import ValidationError
from DentCorpApp.models import Turnos, User

from django import forms
from .models import Turnos
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'image']
class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turnos
        fields = ['fecha_hr_turno', 'autorizado', 'id_serv_odon', 'id_cob_usu', 'id_rol_usu', 'id_asig_cons']

# class TurnoForm(forms.ModelForm):
#     class Meta:
#         model = Turnos
#         fields = '__all__'  # Esto incluirá todos los campos del modelo en el formulario

#     # Validacion personalizada (funcion por cada campo)
#     def clean_titulo(self):
#         titulo = self.cleaned_data.get('titulo')

#         if 'hola' in titulo:
#             raise ValidationError("El titulo no debe contener la palabra 'hola'")

#         return titulo

#     # Validacion personalizada (una funcion para todos los campos) 
#     def clean(self):
#         cleaned_data = super().clean()
#         resumen = cleaned_data.get('resumen')

#         if resumen:
#             if 'mundo' in resumen:
#                 self.add_error('resumen', "El resumen no debe contener la palabra 'mundo'")

#         return cleaned_data