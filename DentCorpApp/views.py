from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import  ListView, DetailView, DeleteView, CreateView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Turnos
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Consultorios
from django.shortcuts import render
from django.contrib import messages
from DentCorpApp.models import User,Coberturas,Consultorios, ServiciosOdontologicos
from .models import Provincias, Ciudades, User
from .forms import SearchForm
from django.contrib.auth.decorators import login_required

# from .forms import CustomUserChangeForm


# from django.http import JsonResponse
# from django.contrib.auth.hashers import check_password
@login_required
def base(request):

    paciente = User.objects.all()
    cobertura = Coberturas.objects.all()
    servicio = ServiciosOdontologicos.objects.all()
    nroConsultorio = Consultorios.objects.all()

    context = {
        'paciente': paciente,
        'cobertura': cobertura,
        'servicio': servicio,
        'nroConsultorio': nroConsultorio,
    }        
    
    return render(request, 'base.html', context) #cambio momentaneo

@login_required
def actualizar_perfil(request):
    if request.method == 'POST':
        # Accede a los datos del formulario
        nuevo_email = request.POST.get('email')

        # Actualiza el correo electrónico del usuario actual
        request.user.email = nuevo_email
        request.user.save()

        # Redirige a la página de perfil o a donde desees
        return redirect('nombre_de_la_url')

    # Resto del código para renderizar el formulario
    return render(request, 'nombre_del_template.html')


def ajustes(request):
    if request.method == 'POST':
        new_email = request.POST.get('email')
        new_imagen = request.POST.get('imagen')
        if new_email:
            request.user.email = new_email
            request.user.save()
            messages.success(request, 'Dirección de correo actualizada exitosamente.')
            return redirect('ajustes')
        if new_imagen:
            request.user.imagen=new_imagen
            request.user.save()
            messages.success(request, 'Foto de perfil actualizada exitosamente.')
            return redirect('ajustes')


    return render(request, 'ajustes/ajustes.html')
# def verificar_contrasena(request):
#     if request.method == 'POST':
#         contrasena_ingresada = request.POST.get('contrasena')
#         contrasena_hash = request.POST.get('hash')
#         es_valida = check_password(contrasena_ingresada, contrasena_hash)
#         return JsonResponse({'es_valida': es_valida})
#     return JsonResponse({'error': 'Método no permitido'}, status=405)

def medicos(request):
    context = {}
    template_name = 'atencion-medica/medicos.html'
    return render(request, template_name)

def pacientes(request):
    context = {}
    template_name = 'atencion-medica/pacientes.html'
    return render(request, template_name)

def servicios_odontologicos(request):
    context = {}
    template_name = 'atencion-medica/servicios-odontologicos.html'
    return render(request, template_name)

def especialidades(request):
    context = {}
    template_name = 'atencion-medica/especialidades.html'
    return render(request, template_name)

def consultorios(request):
    context = {}
    template_name = 'atencion-medica/consultorios.html'
    return render(request, template_name)

class TurnosListView(PermissionRequiredMixin,LoginRequiredMixin, ListView):
    model = Turnos
    template_name = 'atencion-medica/turnos/turnos.html' 
    context_object_name = 'turnos'
    permission_required = 'DentCorpApp.view_turnos'
    
class TurnosDetailView(PermissionRequiredMixin,LoginRequiredMixin, DetailView):
    model = Turnos
    template_name = 'atencion-medica/turnos/turnos_detail.html'
    template_name = 'atencion-medica/turnos/turnos_detail.html'
    context_object_name = 'turno'
    permission_required = 'DentCorpApp.view_turnos'

class TurnosCreateView(PermissionRequiredMixin,LoginRequiredMixin, CreateView):
    model = Turnos
    template_name = 'atencion-medica/turnos/turnos_create.html'
    template_name = 'atencion-medica/turnos/turnos_create.html'
    fields = '__all__'
    success_url = reverse_lazy('turnos')
    success_url = reverse_lazy('turnos')
    success_message = "El turno se ha reservado con éxito."
    permission_required = 'DentCorpApp.add_turnos'

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)
    
class TurnosUpdateView(PermissionRequiredMixin,LoginRequiredMixin, UpdateView):
    model = Turnos
    template_name = 'atencion-medica/turnos/turnos_update.html'
    fields = '__all__'     
    success_url = reverse_lazy('turnos')
    template_name = 'atencion-medica/turnos/turnos_update.html'
    fields = '__all__'     
    success_url = reverse_lazy('turnos')
    success_message = "El turno se ha actualizado con éxito"
    permission_required = 'DentCorpApp.change_turnos'

    def form_valid(self,form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)
    
class TurnosDeleteView(PermissionRequiredMixin,LoginRequiredMixin, DeleteView):
    model = Turnos
    template_name = 'atencion-medica/turnos/turnos_confirm_delete.html'
    success_url = reverse_lazy('turnos')
    template_name = 'atencion-medica/turnos/turnos_confirm_delete.html'
    success_url = reverse_lazy('turnos')
    success_message = "El turno se ha eliminado con éxito"
    permission_required = 'DentCorpApp.delete_turnos'

    def form_valid(self,form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)
    
class SearchView(ListView):
    template_name = 'tu_template.html'
    context_object_name = 'results'
    form_class = SearchForm

    def get_queryset(self):
        form = self.form_class(self.request.GET)
        if form.is_valid():
            search_term = form.cleaned_data.get('search_term')
            if search_term:
                queryset = (
                    Provincias.objects.filter(nom_prov__icontains=search_term) |
                    Ciudades.objects.filter(nom_ciu__icontains=search_term) |
                    User.objects.filter(dni_usu__icontains=search_term) |
                    User.objects.filter(dom_usu__icontains=search_term) |
                    User.objects.filter(tel_usu__icontains=search_term)
                )
                return queryset
        return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class(self.request.GET)
        return context
    
class ConsultoriosListView(ListView):
    model = Consultorios
    template_name = 'atencion-medica/consultorios.html'
    context_object_name = 'consultorios'
        