from django.urls import path
from DentCorpApp import views
from .views import ConsultoriosListView, TurnosCreateView, TurnosDeleteView, TurnosDetailView, TurnosUpdateView, TurnosListView

urlpatterns = [
    path('base', views.base, name= "base"),
    path('turnos/', views.turnos, name = "turnos"),
    path('pacientes/', views.pacientes, name = "pacientes"),
    path('especialidades/', views.especialidades, name = "especialidades"),
    path('medicos/', views.medicos, name = "medicos"),
    path('servicios-odontologicos/', views.servicios_odontologicos, name = "servicios odontologicos"),
    # path('consultorios/', views.consultorios, name = "consultorios"),
    path('consultorios/', ConsultoriosListView.as_view(), name='consultorios'),
    
    
    path('turnos/', TurnosListView.as_view(), name="turnos_list"),
    path('turno/<uuid:pk>/', TurnosDetailView.as_view(), name="turno_detail"),
    path('turno/reservar/', TurnosCreateView.as_view(), name="turno_create"),
    path('turno/modificar/', TurnosUpdateView.as_view(), name="turno_update"),
    path('turno/cancelar/', TurnosDeleteView.as_view(), name="turno_delete"),
]