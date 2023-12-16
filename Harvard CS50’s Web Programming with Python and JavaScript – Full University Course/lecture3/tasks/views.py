from django.http import HttpResponse
from django.shortcuts import render

tasks = ["foo", "bar", "bazz"]

# Create your views here.
def index(request):
    """Index page for tasks app."""
    return render(request, "tasks/index.html", {
        "tasks": tasks, #  the key on the left is what Django templates will use.
    })