from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        # Login form submitted
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login successful
            login(request, user)
            
        else:
            # Login failed
            error_message = 'Invalid username or password'
            return render(request, 'authentication/login.html', {'error_message': error_message})
    else:
        # Display login form
        return render(request, 'authentication/login.html')

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
        reverse('user_logged:login')
    )
    else:
        login(request, user)
        return HttpResponseRedirect(
        reverse('index')
)