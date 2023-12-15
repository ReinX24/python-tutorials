from django.http import HttpResponse
from django.shortcuts import render
import datetime


# Create your views here.

def index(request):
	"""Default page for newyear."""
	now = datetime.datetime.now()
	return render(request, "newyear/index.html", {
		"newyear": now.month == 1 and now.day == 1,
	})


def hello_world(request, name):
	"""Renders hello.html"""
	return render(request, "newyear/hello.html", {
		"name": name.title(),
	})
