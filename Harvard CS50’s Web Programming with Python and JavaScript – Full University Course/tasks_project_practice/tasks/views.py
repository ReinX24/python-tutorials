from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

class NewTaskForm(forms.Form):
    """Class for storing form components."""
    # Creating a text field with a label and classes.
    task_field = forms.CharField(label="New Task", 
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control', 
                                            'placeholder': 'Enter task...'}))

def index(request):
    """Index of our tasks app."""
    # Checks if there are tasks already stored, if not create a new list.
    if "tasks" not in request.session:
        request.session["tasks"] = []
        
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"],
    })

def add(request):
    """Adding stored tasks to our app."""
    # Checks if the request made is POST, from the form.
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        # Checks if the form is valid.
        if form.is_valid():
            new_task = form.cleaned_data["task_field"]
            request.session["tasks"] += [new_task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            # Returns the same page with an error message.
            return render(request, "tasks/add.html", {
                "form": form
            })

    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
