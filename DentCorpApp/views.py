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
from .models import Consultorios, Especialidades, ServiciosOdontologicos, User, Turnos
from django.shortcuts import render
from django.contrib import messages
from DentCorpApp.models import User,Coberturas,Consultorios, ServiciosOdontologicos
from .models import Provincias, Ciudades, User
from .forms import SearchForm,UserProfileForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.views.generic import ListView
from .models import User

from django.contrib.auth.models import Group


class PacientesListView(ListView):
    model = User
    template_name = 'atencion-medica/pacientes/pacientes.html'
    context_object_name = 'users'
    def get_queryset(self):
        
        return User.objects.filter(is_superuser=False, groups__name='paciente')

class PacientesCreateView(PermissionRequiredMixin,LoginRequiredMixin, CreateView):
    model = User
    template_name = 'atencion-medica/pacientes/pacientes_create.html'
    fields = '__all__'
    success_url = reverse_lazy('pacientes')
    success_message = "El paciente se ha registrado con éxito."
    permission_required = ('DentCorpApp.add_user',) 
    fields = ['dni_usu', 'first_name', 'last_name', 'username','dom_usu', 'email', 'id_ciu', 'password']

    def form_valid(self, form):
        response = super().form_valid(form)
        rol_paciente, _ = Group.objects.get_or_create(name='paciente')
        form.instance.groups.add(rol_paciente)
        
        messages.success(self.request, self.success_message)
        return response

class PacientesUpdateView(PermissionRequiredMixin,LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'atencion-medica/pacientes/pacientes_update.html'
    fields = '__all__'     
    success_url = reverse_lazy('pacientes')
    success_message = "Los datos del paciente se han actualizado con éxito"
    permission_required = 'DentCorpApp.change_user'
    fields = ['dni_usu', 'first_name', 'last_name', 'username','dom_usu', 'email', 'id_ciu', 'password']

    def form_valid(self,form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)    

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
        nuevo_email = request.POST.get('email')

        request.user.email = nuevo_email
        request.user.save()

        return redirect('nombre_de_la_url')

    return render(request, 'nombre_del_template.html')


def ajustes(request):
    if request.method == 'POST':
        new_email = request.POST.get('email')
        new_username=request.POST.get("username")
        user_instance = User.objects.get(id=request.user.id)
        user_form = UserProfileForm(request.POST or None, request.FILES or None, instance=user_instance)
        if new_email:
            request.user.email = new_email
            request.user.save()
            messages.success(request, 'Dirección de correo actualizada exitosamente.')
        if new_username:
            request.user.username = new_username
            request.user.save()
            messages.success(request, 'Nombre de usuario actualizado exitosamente.')
        if user_form.is_valid():
            user_form.save()
        return redirect('ajustes')
    else:
        user_form = UserProfileForm(instance=request.user)
    return render(request, 'ajustes/ajustes.html', {'user_form': user_form})


def medicos(request):
    context = {}
    template_name = 'atencion-medica/medicos.html'
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
    context_object_name = 'turno'
    permission_required = 'DentCorpApp.view_turnos'

class TurnosCreateView(PermissionRequiredMixin,LoginRequiredMixin, CreateView):
    model = Turnos
    template_name = 'atencion-medica/turnos/turnos_create.html'
    fields = '__all__'
    success_url = reverse_lazy('turnos')
    success_message = "El turno se ha reservado con éxito."
    permission_required = ('DentCorpApp.add_turnos',) 

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)
    
class TurnosUpdateView(PermissionRequiredMixin,LoginRequiredMixin, UpdateView):
    model = Turnos
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

    
class ConsultoriosListView(LoginRequiredMixin, ListView):
    model = Consultorios
    template_name = 'atencion-medica/consultorios.html'
    context_object_name = 'consultorios'

class EspecialidadesListView(LoginRequiredMixin, ListView):
    model = Especialidades
    template_name='atencion-medica/especialidades.html'
    context_object_name = 'especialidades'

class ServiciosOdontologicosListView(LoginRequiredMixin, ListView):
    model = ServiciosOdontologicos
    template_name='atencion-medica/servicios-odontologicos.html'
    context_object_name = 'servicios'
    
    
