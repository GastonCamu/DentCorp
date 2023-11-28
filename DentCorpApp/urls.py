from django.urls import path
from DentCorpApp import views
from .views import ConsultoriosListView, PacientesListView, PacientesUpdateView,EspecialidadesListView, ServiciosOdontologicosListView, PacientesListView,PacientesCreateView , TurnosDeleteView, TurnosListView, TurnosCreateView, TurnosUpdateView
urlpatterns = [
    path('index', views.index, name= "index"),
    path('ajustes', views.ajustes, name = "ajustes"),
    path('especialidades/', EspecialidadesListView.as_view(), name = "especialidades"),
    path('medicos/', views.medicos, name = "medicos"),
    path('servicios-odontologicos/', ServiciosOdontologicosListView.as_view(), name = "servicios odontologicos"),
    
    path('consultorios/', ConsultoriosListView.as_view(), name='consultorios'),
    path('turnos/', TurnosListView.as_view(), name="turnos"),
    path('turnos/reservar/', TurnosCreateView.as_view(), name="turno_create"),
    path('turno/modificar/<pk>/', TurnosUpdateView.as_view(), name="turno_update"),
    path('turno/cancelar/<pk>/', TurnosDeleteView.as_view(), name="turno_delete"),

    path('pacientes/', PacientesListView.as_view(), name="pacientes"),
    path('pacientes/registrar/', PacientesCreateView.as_view(), name="paciente_create"),
    path('pacientes/modificar/<pk>/', PacientesUpdateView.as_view(), name="paciente_update"),

    path('pacientes/resultado/', views.search, name="paciente_buscar" ),
    path('turnos/resultado/', views.search_turno, name="turno_buscar" ),
]