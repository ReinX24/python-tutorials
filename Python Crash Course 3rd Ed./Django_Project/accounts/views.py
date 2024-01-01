from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
    """Registering a new user for our web site."""
    if request.method != "POST":
        # Display a blank registration form
        form = UserCreationForm()
    else:
        # Process a completed form when a POST method is received
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            # Saving the form's data to our database and storing the data in
            # new_user, this stores a user object.
            new_user = form.save()
            # Log the user in and then redirect to home page.
            login(request, new_user)
            return redirect("learning_logs:index")

    # Display a blank or invalid form is the method is not POST.
    context = {"form": form}
    return render(request, "registration/register.html", context)
