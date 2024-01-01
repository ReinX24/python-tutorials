from django.urls import include, path

from . import views

app_name = "accounts"
urlpatterns = [
    # Login and logout pages built in Django
    path("", include("django.contrib.auth.urls")),
    # Register page for new users to register an account
    path("register/", views.register, name="register"),
]
