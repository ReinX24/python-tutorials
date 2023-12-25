from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def index(request):
    """Index page of our users app."""
    # Checking if the user is authenticated.
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")

def login_view(request):
    """Login page of our users app."""
    if request.method == "POST":
        # Getting the user's information
        username = request.POST["username"]
        password = request.POST["password"]
        
        # Autheticating the user's information.
        user = authenticate(request, username=username, password=password)
        
        # Checking if the authentication is successful.
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid credentials."
            })

    return render(request, "users/login.html")

def logout_view(request):
    """Logout page of our users app."""
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged out"
    })