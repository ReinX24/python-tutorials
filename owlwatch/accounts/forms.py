from django.forms import EmailField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms


class RegisterForm(UserCreationForm):
    """Custom Register form with email."""
    email = EmailField(label=("Email address"), required=True, help_text=("Required."))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    """Custom Login form with email."""
    username = forms.CharField(label='Email / Username')