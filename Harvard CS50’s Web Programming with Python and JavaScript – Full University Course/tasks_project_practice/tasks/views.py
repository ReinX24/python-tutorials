from django.shortcuts import render

def index(request):
    """Index of our tasks app."""
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"],
    })

def add(request):
    """Adding stored tasks to our app."""
    return render(request, "tasks/add.html")
