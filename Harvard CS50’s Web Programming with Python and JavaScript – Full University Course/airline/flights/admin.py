from django.contrib import admin

from .models import Flight, Airport, Passenger

# Register your models here.
class AirportAdmin(admin.ModelAdmin):
    """Class for configuring our Flight page at admin page."""
    list_display = ("city", "code")

class FlightAdmin(admin.ModelAdmin):
    """Class for configuring our Flight page at admin page."""
    # This displays certain attributes in the admin page.
    list_display = ("id", "origin", "destination", "duration")

class PassengerAdmin(admin.ModelAdmin):
    """Class for configuring our Passenger page at admin page."""
    # Adding a filter menu when we go to each of our Passenger's flights. 
    filter_horizontal = ("flights",)


# This allows the admin app to manipulate Airport and Flight instances.
admin.site.register(Airport, AirportAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)