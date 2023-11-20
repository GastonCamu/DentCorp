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


@login_required
def home(request):
    context = {}
    return render(request, 'base.html') #cambio momentaneo

class TurnosListView(LoginRequiredMixin, ListView):
    model = Turnos
    template_name = 'atencion-medica/turnos.html'
    context_object_name = 'turnos'
    paginate_by = 4

    def get_queryset(self):
        return Turnos.objetcs.filter(estado = 'r')
    
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