from django.urls import path, include

from journal import views

app_name = "journal"
urlpatterns = [
    path("entries/<int:user_id>/", views.entries, name="entries"),
]