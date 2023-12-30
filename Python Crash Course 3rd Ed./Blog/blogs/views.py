from django.shortcuts import render

# Create your views here.
def index(request):
    """Index page for our Blog."""
    return render(request, 'blogs/index.html')