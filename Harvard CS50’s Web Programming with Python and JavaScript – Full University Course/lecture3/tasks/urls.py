from django.urls import path
from . import views

app_name = "tasks"
urlpatterns = [
	# Root directory path, name parameter is optional.
	path("", views.index, name="index"),
	path("add", views.add, name="add"),
]
