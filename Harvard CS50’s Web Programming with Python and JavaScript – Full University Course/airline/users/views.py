from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    """Index page of our users app."""
    return render(request, "users/index.html")

def login_view(request):
    """Login page of our users app."""

def logout_view(request):
    """Logout page of our users app."""