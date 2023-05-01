from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm
from django.http import HttpResponse

# Create your views here.

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
            #return HttpResponse("Registration successful")
    else:
        form = RegistrationForm()
    return render(request, 'user_registration/register.html', {'form': form})