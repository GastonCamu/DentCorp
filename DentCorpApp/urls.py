from django.urls import path
from DentCorpApp import views
from .views import ConsultoriosListView, TurnosCreateView, TurnosDeleteView, TurnosDetailView, TurnosUpdateView, TurnosListView
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    path('base', views.base, name= "base"),
    # path('turnos/', views.turnos, name = "turnos"),
    path('pacientes/', views.pacientes, name = "pacientes"),
    path('especialidades/', views.especialidades, name = "especialidades"),
    path('medicos/', views.medicos, name = "medicos"),
    path('servicios-odontologicos/', views.servicios_odontologicos, name = "servicios odontologicos"),
    # path('consultorios/', views.consultorios, name = "consultorios"),
    path('consultorios/', ConsultoriosListView.as_view(), name='consultorios'),
    
    
    
    path('turnos/', TurnosListView.as_view(), name="turnos"),
    path('turnos/<uuid:pk>/', TurnosDetailView.as_view(), name="turno_detail"),
    path('turnos/reservar/', TurnosCreateView.as_view(), name="turno_create"),
    path('turnos/modificar/<uuid:pk>/', TurnosUpdateView.as_view(), name="turno_update"),
    path('turnos/cancelar/<uuid:pk>/', TurnosDeleteView.as_view(), name="turno_delete"),

    path('ajustes',views.ajustes,name="ajustes"),
    # path('verificar_contrasena/', views.verificar_contrasena, name='verificar_contrasena'),

    # path('',UserListView.as_view(),name="user"),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


