from django.urls import path
from . import views  # importing the views module.

urlpatterns = [
	# Root directory path, name parameter is optional.
	path("", views.index, name="index"),  # http://127.0.0.1:8000/newyear
	path("<str:name>", views.hello_world, name="helloworld")
]
