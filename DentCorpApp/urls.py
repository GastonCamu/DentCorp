from django.urls import path
from DentCorpApp import views
from .views import ConsultoriosListView, EspecialidadesListView, ServiciosOdontologicosListView, PacientesListView
urlpatterns = [
    path('base', views.base, name= "base"),
    path('turnos/', views.turnos, name = "turnos"),
    path('pacientes/', views.pacientes, name = "pacientes"),
    path('especialidades/', EspecialidadesListView.as_view(), name = "especialidades"),
    path('medicos/', views.medicos, name = "medicos"),
    path('servicios-odontologicos/', ServiciosOdontologicosListView.as_view(), name = "servicios odontologicos"),
    # path('consultorios/', views.consultorios, name = "consultorios"),
    path('consultorios/', ConsultoriosListView.as_view(), name='consultorios'),
    path('pacientes/', PacientesListView.as_view(), name='pacientes'),
    
    
    # path('turnos/', views.TurnosListView.as_view(), name="turnos_list"),
    # path('turnos/<uuid:pk>/', views.TurnosDetailView.as_view(), name="turnos_detail"),
    # path('turnos/', views.TurnosCreateView.as_view(), name="turnos_create"),
    # path('turnos/', views.TurnosUpdateView.as_view(), name="turnos_update"),
    # path('turnos/', views.TurnosDeleteView.as_view(), name="turnos_delete"),
]