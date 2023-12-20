from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse

import tasks

# tasks = ["foo", "bar", "bazz"]
# tasks = []

class NewTaskForm(forms.Form):
    "Class for creating form elements."
    # This utilizes django's built in form validation features where it checks
    # if an input is a number or if the field is empty.
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)

# Create your views here.
def index(request):
    """Index page for tasks app."""
    # Checking if 'tasks' exists in the current session.
    if "tasks" not in request.session:
        # Adding an empty list to our current session.
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"], #  the key on the left is what Django templates will use.
    })

def add(request):
    """Render tasks and add to app."""
    # Checks if a POST request is made in our add page.
    if request.method == "POST":
        # Stores the data that the user sends when they post a form.
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]

            # Redirecting the user back to our index page.
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            # If the form is not valid, send back form to user, this
            # will show them error messages regarding their inputs.
            return render(request, "tasks/add.html", {
                # Sends back existing form data.
                "form": form
            })

    # This is returned when the page is loaded.
    return render(request, "tasks/add.html", {
        # This html has an instance of our NewTaskForm class.
        "form": NewTaskForm()
    })