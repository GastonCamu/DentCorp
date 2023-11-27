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
from .forms import SearchForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# from .forms import CustomUserChangeForm


# from django.http import JsonResponse
# from django.contrib.auth.hashers import check_password


# class UserListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
#     model = User
#     template_name = 'partials/navbar.html' 
#     context_object_name = 'users'

#     def get_queryset(self):
#         return User.objects.filter(id=self.request.user.id)
    

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

class PacientesListView(PermissionRequiredMixin,LoginRequiredMixin, ListView):
    model = User
    template_name = 'atencion-medica/pacientes.html'
    context_object_name = 'usuarios'
    permission_required = ('DentCorpApp.view_user',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context    

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
    
class PacientesListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'atencion-medica/pacientes.html'
    context_object_name = 'pacientes'
    
def index(request):
    conspaci=Turnos.objects.filter(estado__exact='d')
    

# class TurnosDetailView(LoginRequiredMixin, DetailView):
#     model = Turnos
#     template_name = 'templates/turnos_detail.html'
#     context_object_name = 'det_turno'

# class TurnosCreateView(LoginRequiredMixin, CreateView):
#     model = Turnos
#     template_name = 'templates/turnos_create.html'
#     fields = '__all__'
#     success_url = reverse_lazy('turnos_list')
#     success_message = "El turno se ha reservado con éxito."

#     def form_valid(self, form):
#         messages.success(self.request, self.success_message)
#         return super().form_valid(form)
    
# class TurnosUpdateView(LoginRequiredMixin, UpdateView):
#     model = Turnos
#     template_name = 'template/turnos_update.html'
#     fields = '__all__'
#     success_url = reverse_lazy('turnos_list')
#     success_message = "El turno se ha actualizado con éxito"

#     def form_valid(self,form):
#         messages.success(self.request, self.success_message)
#         return super().form_valid(form)
    
# class TurnosDeleteView(LoginRequiredMixin, DeleteView):
#     model = Turnos
#     template_name = 'template/turnos_confirm_delete.html'
#     fields = '__all__'
#     success_url = reverse_lazy('turnos_list')
#     success_message = "El turno se ha eliminado con éxito"

#     def form_valid(self,form):
#         messages.success(self.request, self.success_message)
#         return super().form_valid(form)