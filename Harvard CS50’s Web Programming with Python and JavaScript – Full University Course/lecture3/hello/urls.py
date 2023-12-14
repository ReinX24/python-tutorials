from django.urls import path
from . import views  # importing the views module.

urlpatterns = [
	# Root directory path, name parameter is optional.
	path("", views.index, name="index"),  # http://127.0.0.1:8000/hello/
	# Adding another path, path(site_path, module_function, name="optional").
	path("rein", views.rein, name="rein"),  # http://127.0.0.1:8000/hello/rein
	path("reinne", views.reinne, name="reinne"),
	# http://127.0.0.1:8000/hello/reinne
	path("<str:name>", views.greet, name="greet"),
	# Prints passed in name, http://127.0.0.1:8000/hello/custom_name
]
