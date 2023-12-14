from django.urls import path
from . import views  # importing the views module.

urlpatterns = [
	# Root directory path, name parameter is optional.
	path("", views.index, name="index"),  # http://127.0.0.1:8000/hello/
	# Adding another path, path(site_path, module_function, name="optional").
	# http://127.0.0.1:8000/hello/rein
	path("rein", views.rein, name="rein"),
	# http://127.0.0.1:8000/hello/reinne
	path("reinne", views.reinne, name="reinne"),
	# Prints passed in name, http://127.0.0.1:8000/hello/CUSTOM_NAME
	path("<str:name>", views.greet, name="greet"),
	# Prints in passed age, http://127.0.0.1:8000/hello/age/ENTERED_AGE
	path("age/<int:age>", views.age, name="age"),
]
