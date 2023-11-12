from django.urls import path
from DentCorpApp import views

urlpatterns = [
    path('', views.home, name= "home"),
    path('turnos/', views.turnos, name = "turnos"),
    path('base', views.base, name = "base"),
    path('tabla', views.tabla, name = "tabla"),
]