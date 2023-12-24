from django.contrib import admin

from .models import Flight, Airport, Passenger

# Register your models here.

# This allows the admin app to manipulate Airport and Flight instances.
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Passenger)