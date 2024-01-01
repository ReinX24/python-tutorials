from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
    """Register a new user to our blog website."""
    if request.method != "POST":
        # Display a blank registration form.
        form = UserCreationForm()
    else:
        # Process the form when a POST method is received.
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("blogs:index")

    context = {"form": form}
    return render(request, "registration/register.html", context)
