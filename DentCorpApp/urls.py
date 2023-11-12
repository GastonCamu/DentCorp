from django.urls import path
from DentCorpApp import views

urlpatterns = [
    path('base', views.base, name= "base"),
    path('turnos/', views.turnos, name = "turnos"),
    
    # path('turnos/', views.TurnosListView.as_view(), name="turnos_list"),
    # path('turnos/<uuid:pk>/', views.TurnosDetailView.as_view(), name="turnos_detail"),
    # path('turnos/', views.TurnosCreateView.as_view(), name="turnos_create"),
    # path('turnos/', views.TurnosUpdateView.as_view(), name="turnos_update"),
    # path('turnos/', views.TurnosDeleteView.as_view(), name="turnos_delete"),
]