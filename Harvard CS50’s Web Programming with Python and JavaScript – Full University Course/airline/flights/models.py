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
    """For storing the different attributes that each flight will have."""
    # origin = models.CharField(max_length=64)
    # Using foreign keys to reference data from other tables
    # models.CASCADE deletes all data relating to deleted record
    # related_name is used to check for all flights with a similar origin
    # Think of ForeignKey as objects that have attributes, in this case a city and a code.
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures") 
    # destination = models.CharField(max_length=64)
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        # Returns a string representation of the Flight object
        return f"{self.id}: {self.origin} to {self.destination}"