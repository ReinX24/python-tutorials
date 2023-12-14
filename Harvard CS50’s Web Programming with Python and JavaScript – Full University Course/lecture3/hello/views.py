from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
	"""Prints 'Hello!' to the webpage."""
	# return HttpResponse("Hello!")  # stored in webpage body tag.

	# This finds the file in the templates/hello directory.
	# Note: when rendering an html from an app folder, go to the settings of
	# the project folder and add app folder to INSTALLED_APPS for it to render
	# the html file.
	return render(request, "hello/index.html")  # renders html file


def rein(request):
	"""Prints 'Hello, Rein!' to the webpage."""
	return HttpResponse("Hello, Rein!")


def reinne(request):
	"""Prints 'Hello, Reinne!' to the webpage."""
	return HttpResponse("Hello, Reinne!")


def greet(request, name):
	"""Greets the name in the parameter."""
	# return HttpResponse(f"Hello, {name.title()}!")
	# Passing in an html file and parameters for that html file to use.
	return render(request, "hello/greet.html", {
		"name": name.title(),  # takes passed name in the url
	})


def age(request, age):
	"""Tell age entered in url."""
	return render(request, "hello/age.html", {
		"age": age
	})
