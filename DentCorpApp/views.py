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
from .models import Consultorios, Especialidades, ServiciosOdontologicos
from django.shortcuts import render

@login_required

def base(request):
    context = {}
    return render(request, 'base.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'registration/register.html', {'form': CustomUserCreationForm})
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            user = authenticate(
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password']
            )
            login(request, user)

            return redirect('home')
        else:
            return render(request, 'registration/register.html', {"form":form})
        

def turnos(request):
    context = {}
    template_name = 'atencion-medica/turnos.html'
    return render(request, template_name)

def register(request):
    if request.method == 'GET':
        return render(request, 'registration/register.html', {'form': CustomUserCreationForm})

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
  
            user = authenticate(
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password1']       
            )
            login(request, user)


            return redirect('base')
        else:
            return render(request, 'registration/register.html', {"form": form})
        
@login_required
def base(request):
    context = {}
    
    return render(request, 'base.html', context)

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
    template_name = 'atencion-medica/turnos.html' 
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

class EspecialidadesListView(ListView):
    model = Especialidades
    template_name='atencion-medica/especialidades.html'
    context_object_name = 'especialidades'

class ServiciosOdontologicosListView(ListView):
    model = ServiciosOdontologicos
    template_name='atencion-medica/servicios-odontologicos.html'
    context_object_name = 'servicios'
    
    
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