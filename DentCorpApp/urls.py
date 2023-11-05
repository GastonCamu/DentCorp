from django.urls import path
from DentCorpApp import views

urlpatterns = [
    path('', views.home, name= "home")
]