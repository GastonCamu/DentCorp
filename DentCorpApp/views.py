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

from django.shortcuts import render, get_object_or_404, redirect
from .models import Especialidades
from .forms import EspecialidadesForm


@login_required
def home(request):
    context = {}
    return render(request, 'base.html')

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
    template_name = 'atencion-medica/turnos.html'
    context_object_name = 'turnos'
    paginate_by = 4

# class TurnosListView(LoginRequiredMixin, ListView):
#     model = Turnos
#     template_name = 'templates/turnos_list.html'
#     context_object_name = 'turnos'
#     paginate_by = 4

    # def get_queryset(self):
    #     return Turnos.objetcs.filter(estado = 'r')
    

class TurnosDetailView(LoginRequiredMixin, DetailView):
    model = Turnos
    template_name = 'templates/turnos_detail.html'
    context_object_name = 'det_turno'

class TurnosCreateView(LoginRequiredMixin, CreateView):
    model = Turnos
    template_name = 'templates/turnos_create.html'
    fields = '__all__'
    success_url = reverse_lazy('turnos_list')
    success_message = "El turno se ha reservado con éxito."

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)
    
class TurnosUpdateView(LoginRequiredMixin, UpdateView):
    model = Turnos
    template_name = 'template/turnos_update.html'
    fields = '__all__'
    success_url = reverse_lazy('turnos_list')
    success_message = "El turno se ha actualizado con éxito"

    def form_valid(self,form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)
    
class TurnosDeleteView(LoginRequiredMixin, DeleteView):
    model = Turnos
    template_name = 'template/turnos_confirm_delete.html'
    fields = '__all__'
    success_url = reverse_lazy('turnos_list')
    success_message = "El turno se ha eliminado con éxito"

    def form_valid(self,form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)
    

def especialidades_list(request):
    especialidades = Especialidades.objects.all()
    return render(request, 'especialidades_list.html', {'especialidades': especialidades})

def especialidades_detail(request, pk):
    especialidad = get_object_or_404(Especialidades, pk=pk)
    return render(request, 'especialidades_detail.html', {'especialidad': especialidad})

def especialidades_new(request):
    if request.method == "POST":
        form = EspecialidadesForm(request.POST)
        if form.is_valid():
            especialidad = form.save(commit=False)
            especialidad.save()
            return redirect('especialidades_detail', pk=especialidad.pk)
    else:
        form = EspecialidadesForm()
    return render(request, 'especialidades_edit.html', {'form': form})

def especialidades_edit(request, pk):
    especialidad = get_object_or_404(Especialidades, pk=pk)
    if request.method == "POST":
        form = EspecialidadesForm(request.POST, instance=especialidad)
        if form.is_valid():
            especialidad = form.save(commit=False)
            especialidad.save()
            return redirect('especialidades_detail', pk=especialidad.pk)
    else:
        form = EspecialidadesForm(instance=especialidad)
    return render(request, 'especialidades_edit.html', {'form': form})

def especialidades_delete(request, pk):
    especialidad = get_object_or_404(Especialidades, pk=pk)
    especialidad.delete()
    return redirect('especialidades_list')