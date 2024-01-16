from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import views as auth_views

# from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegisterForm, LoginForm
from app_owlwatch.models import Questions, Averages


# Create your views here.
def register(request):
    """Registering a new user for our web site."""
    if request.method != "POST":
        # Display a blank registration form
        form = RegisterForm()
    else:
        # Process a completed form when a POST method is received
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            # Saving the form's data to our database and storing the data in
            # new_user, this stores a user object.
            new_user = form.save()

            # When the user makes a new account, creat an instance of Questions
            # and Averages already, this is so that there will only be one
            # instance instead of several instances of their averages and test
            # answers.
            questions = Questions()
            questions.owner = new_user
            questions.save()

            averages = Averages()
            averages.owner = new_user
            averages.save()

            # Log the user in and then redirect to home page.
            login(request, new_user)
            return redirect("app_owlwatch:index")

    # Display a blank or invalid form is the method is not POST.
    context = {"form": form}
    return render(request, "registration/register.html", context)
