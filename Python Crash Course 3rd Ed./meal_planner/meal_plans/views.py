from django.shortcuts import render

# Create your views here.
def index(request):
    """Index page for our meal_plans app."""
    return render(request, 'meal_plans/index.html')
