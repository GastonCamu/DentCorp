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

       

# def turnos(request):
#     context = {}
#     template_name = 'atencion-medica/turnos.html'
#     return render(request, template_name)


        

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
    template_name = 'atencion-medica/turnos.html' 
    context_object_name = 'turnos'
    permission_required = ('DentCorpApp.view_turnos',) 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    # def get_queryset(self):
    #     return Turnos.objetcs.filter(estado = 'r')
    
class ConsultoriosListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Consultorios
    template_name = 'atencion-medica/consultorios.html'
    context_object_name = 'consultorios'
    permission_required = 'DentCorpApp.view_consultorios'
    
class TurnosDetailView(PermissionRequiredMixin,LoginRequiredMixin, DetailView):
    model = Turnos
    template_name = 'turnos/turnos_detail.html'
    context_object_name = 'turno'
    permission_required = ('DentCorpApp.view_turnos',) 

class TurnosCreateView(PermissionRequiredMixin,LoginRequiredMixin, CreateView):
    model = Turnos
    template_name = 'turnos/turnos_create.html'
    fields = '__all__'
    success_url = reverse_lazy('turnos')
    success_message = "El turno se ha reservado con éxito."
    permission_required = ('DentCorpApp.add_turnos',) 

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)
    
class TurnosUpdateView(PermissionRequiredMixin,LoginRequiredMixin, UpdateView):
    model = Turnos
    template_name = 'turnos/turnos_update.html'
    fields = '__all__'     
    success_url = reverse_lazy('turno')
    success_message = "El turno se ha actualizado con éxito"
    permission_required = 'DentCorpApp.change_turnos'

    def form_valid(self,form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)
    
class TurnosDeleteView(PermissionRequiredMixin,LoginRequiredMixin, DeleteView):
    model = Turnos
    template_name = 'turnos/turnos_confirm_delete.html'
    success_url = reverse_lazy('turnos_list')
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
