from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def home(request):
    context = {}
    return render(request, 'home/index.html')

def base(request):
    context = {}
    return render(request, 'base.html')

def turnos(request):
    context = {}
    template_name = 'atencion-medica/turnos.html'
    return render(request, template_name)

def tabla(request):
    context = {}
    template_name = 'atencion-medica/tabla.html'
    return render(request, template_name)