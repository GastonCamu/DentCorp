from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import  ListView, DetailView, DeleteView, CreateView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Turnos
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Consultorios
from django.shortcuts import render
from django.contrib import messages
from DentCorpApp.models import User,Coberturas,Consultorios, ServiciosOdontologicos


@login_required
def base(request):

    paciente = User.objects.all().count()
    cobertura = Coberturas.objects.all().count()
    servicio = ServiciosOdontologicos.objects.all().count()
    nroConsultorio = Consultorios.objects.all().count()


    context = {
        'paciente': paciente,
        'cobertura': cobertura,
        'servicio': servicio,
        'nroConsultorio': nroConsultorio,
    }        
    
    return render(request, 'base.html', context) #cambio momentaneo

       

def turnos(request):
    context = {}
    template_name = 'atencion-medica/turnos.html'
    return render(request, template_name)


        

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

class TurnosListView(LoginRequiredMixin, ListView):
    model = Turnos
    template_name = 'turnos/turnos_list.html' 
    context_object_name = 'turnos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get_queryset(self):
        return Turnos.objetcs.filter(estado = 'r')
    
class ConsultoriosListView(ListView):
    model = Consultorios
    template_name = 'atencion-medica/consultorios.html'
    context_object_name = 'consultorios'
    
    
class TurnosDetailView(LoginRequiredMixin, DetailView):
    model = Turnos
    template_name = 'turnos/turnos_detail.html'
    context_object_name = 'turno'

class TurnosCreateView(LoginRequiredMixin, CreateView):
    model = Turnos
    template_name = 'turnos/turnos_create.html'
    fields = '__all__'
    success_url = reverse_lazy('turnos_list')
    success_message = "El turno se ha reservado con éxito."

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)
    
class TurnosUpdateView(LoginRequiredMixin, UpdateView):
    model = Turnos
    template_name = 'turnos/turnos_update.html'
    fields = '__all__'
    success_url = reverse_lazy('turnos_list')
    success_message = "El turno se ha actualizado con éxito"

    def form_valid(self,form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)
    
class TurnosDeleteView(LoginRequiredMixin, DeleteView):
    model = Turnos
    template_name = 'turnos/turnos_confirm_delete.html'

    success_url = reverse_lazy('turnos_list')
    success_message = "El turno se ha eliminado con éxito"

    def form_valid(self,form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)