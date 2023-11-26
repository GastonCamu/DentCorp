from django.urls import path
from DentCorpApp import views
from .views import ConsultoriosListView, EspecialidadesListView, ServiciosOdontologicosListView, PacientesCreateView,PacientesListView, TurnosListView, TurnosCreateView, TurnosUpdateView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('base', views.base, name= "base"),
    path('ajustes', views.ajustes, name = "ajustes"),
    path('especialidades/', EspecialidadesListView.as_view(), name = "especialidades"),
    path('medicos/', views.medicos, name = "medicos"),
    path('servicios-odontologicos/', ServiciosOdontologicosListView.as_view(), name = "servicios odontologicos"),
    
    path('consultorios/', ConsultoriosListView.as_view(), name='consultorios'),

    path('turnos/', TurnosListView.as_view(), name="turnos"),
    path('turnos/reservar/', TurnosCreateView.as_view(), name="turno_create"),
    path('turno/modificar/<uuid:pk>/', TurnosUpdateView.as_view(), name="turno_update"),
    # path('turno/cancelar/', TurnosDeleteView.as_view(), name="turno_delete"),
    path('pacientes/', PacientesListView.as_view(), name="pacientes"),
    path('pacientes/registrar/', PacientesCreateView.as_view(), name="pacientes_create"),
    
]