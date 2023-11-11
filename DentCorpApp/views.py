from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

def home(request):
    context = {}
    return render(request, 'home/index.html')

# autenticacion
def register(request):
    if request.method == 'GET':
        return render(request, 'registration/register.html', {'form': CustomUserCreationForm})
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            
            user = authenticate (
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1']
            )
            login(request, user)
            
            return redirect('home')
    else:
         
         return render(request, 'registration/register.html', {"form": form})
     

# aplicacion
@login_required
def home(request):
    context = {}
    
    return render (request, 'home/base.html', context)