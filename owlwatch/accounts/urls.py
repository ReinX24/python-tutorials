from django.urls import path, include

from accounts import views

app_name = "accounts"
urlpatterns = [
    # Default auth urls from Django.
    path("", include("django.contrib.auth.urls")),
    # Registration page.
    path("register/", views.register, name="register"),
]
