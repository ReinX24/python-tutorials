from django.urls import path
from . import views

urlpatterns = [
	# Root directory path, name parameter is optional.
	# http://127.0.0.1:8000/newyear
	path("", views.index, name="index"),
	path("<str:name>", views.hello_world, name="helloworld"),
]
