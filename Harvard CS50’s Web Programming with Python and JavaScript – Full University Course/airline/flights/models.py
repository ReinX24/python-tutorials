from django.db import models

# Create your models here.
class Airport(models.Model):
    """For storing different attributes for airports."""
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        """String representation for airport instances."""
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    """
    For storing the different attributes that each flight will have to our 
    database.
    """
    # origin = models.CharField(max_length=64)
    # Using foreign keys to reference data from other tables
    # models.CASCADE deletes all data relating to deleted record
    # related_name is used to check for all flights with a similar origin
    # ForeignKey are objects that have attributes (city and code).
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, 
                               related_name="departures") 
    # destination = models.CharField(max_length=64)
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, 
                                    related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        """ Returns a string representation of the Flight object """
        return f"{self.id}: {self.origin} to {self.destination}"
    
    def is_valid_flight(self):
        """
        Checks if the flight is valid by checking if the origin is not the same 
        with the destination and if the duration is greater than or equal to 0.
        """
        return self.origin != self.destination and self.duration >= 0

class Passenger(models.Model):
    """
    For storing passenger attributes to our database.
    This model creates two tables in our database, one for our passenger and 
    another table using the id of our passengers as a reference to what flights
    they have recorded. Flights objects also have access to the flights related
    to each passenger that we have stored in our database (check views.py 
    flight function return statement).
    """
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    # Making each passenger have the ability to be on multiple flights 
    # (ManyToManyField), the passenger is also allowed to not have a flight 
    # stored (blank=True).
    flights = models.ManyToManyField(Flight, blank=True, 
                                     related_name="passengers")
    
    def __str__(self):
        """String representation for our Passenger instances."""
        return f"{self.first} {self.last}"
