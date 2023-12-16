from django.urls import path
from . import views

urlpatterns = [
	# Root directory path, name parameter is optional.
	path("", views.index, name="index"),
]
