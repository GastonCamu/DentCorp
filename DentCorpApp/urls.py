from django.urls import path
from DentCorpApp import views
from .views import ConsultoriosListView, EspecialidadesListView, ServiciosOdontologicosListView, PacientesListView, TurnosListView, TurnosCreateView
urlpatterns = [
    path('base', views.base, name= "base"),
    path('pacientes/', views.pacientes, name = "pacientes"),
    path('especialidades/', EspecialidadesListView.as_view(), name = "especialidades"),
    path('medicos/', views.medicos, name = "medicos"),
    path('servicios-odontologicos/', ServiciosOdontologicosListView.as_view(), name = "servicios odontologicos"),
    # path('consultorios/', views.consultorios, name = "consultorios"),
    path('consultorios/', ConsultoriosListView.as_view(), name='consultorios'),
    path('pacientes/', PacientesListView.as_view(), name='pacientes'),
    path('turnos/', TurnosListView.as_view(), name = "turnos"),
    path('turno/reservar/', TurnosCreateView.as_view(), name="turno_create"),
    
    
    # path('turnos/', TurnosListView.as_view(), name="turnos_list"),
    # path('turno/<uuid:pk>/', TurnosDetailView.as_view(), name="turno_detail"),
    # path('turno/reservar/', TurnosCreateView.as_view(), name="turno_create"),
    # path('turno/modificar/<uuid:pk>/', TurnosUpdateView.as_view(), name="turno_update"),
    # path('turno/cancelar/<uuid:pk>/', TurnosDeleteView.as_view(), name="turno_delete"),
]