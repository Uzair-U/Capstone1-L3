from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm
from django.http import HttpResponse

# Create your views here.

def register_user(request):
    """Registers a new user with the provided user registration form and logs them in.

    :param request: The HTTP request object.
    :type request: django.http.HttpRequest
    :returns: If the form is valid, redirects the user to the 'index' view; otherwise, renders the registration form again with the validation errors.
    :rtype: django.shortcuts.redirect or django.shortcuts.render
    """
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