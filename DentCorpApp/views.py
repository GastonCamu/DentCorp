from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

def home(request):
    context = {}
    return render(request, 'home/index.html')

def base(request):
    context = {}
    return render(request, 'base.html')