from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
	"""Prints 'Hello!' to the webpage."""
	return HttpResponse("Hello!")  # stored in webpage body tag.


def rein(request):
	"""Prints 'Hello, Rein!' to the webpage."""
	return HttpResponse("Hello, Rein!")


def reinne(request):
	"""Prints 'Hello, Reinne!' to the webpage."""
	return HttpResponse("Hello, Reinne!")


def greet(request, name):
	"""Greets the name in the parameter."""
	return HttpResponse(f"Hello, {name.title()}!")
