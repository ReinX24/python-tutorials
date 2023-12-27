from django import forms
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from .models import Flight, Passenger

# Create your views here.
def index(request):
    """Index of our flights app."""
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    """Render the attributes of a specific flight."""
    try:
        flight = Flight.objects.get(pk=flight_id) # pk means primary key
    except Flight.DoesNotExist:
        raise Http404("Flight not found.")
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        # Excluding all passengers in our database who are already on the 
        # current flight.
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })

def book(request, flight_id):
    if request.method == "POST":
        booked_flight = Flight.objects.get(pk=flight_id)

        # Getting the new passenger object from a form that returns the 
        # passenger id.
        new_passenger = Passenger.objects.get(
                pk=int(request.POST["passenger"])
            )

        # Adding a flight to our new Passenger instance.
        new_passenger.flights.add(booked_flight)

        # After the user has booked a flight, return to the flight page.
        return HttpResponseRedirect(reverse("flight", 
                                            args=(booked_flight.id,)))