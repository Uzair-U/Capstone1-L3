from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

# Create your views here.

def user_login(request):
    """Logs in a user if the provided credentials are valid.

    If the login is successful, the user is redirected to the home page.
    If the login fails, the user is redirected to the login page with an error message.

    :param HttpRequest request: The HTTP request object
    :returns: The HTTP response object
    :rtype: HttpResponse
    """
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
    """Authenticates a user based on the provided credentials.

    If the authentication is successful, the user is redirected to the home page.
    If the authentication fails, the user is redirected to the login page.

    :param HttpRequest request: The HTTP request object
    :returns: The HTTP response object
    :rtype: HttpResponse
    """
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