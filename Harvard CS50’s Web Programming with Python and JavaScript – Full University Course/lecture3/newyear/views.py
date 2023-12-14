from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
	"""Default page for newyear."""
	return HttpResponse("NEW YEAR!")


def hello_world(request, name):
	"""Renders hello.html"""
	return render(request, "newyear/hello.html", {
		"name": name.title(),
	})
