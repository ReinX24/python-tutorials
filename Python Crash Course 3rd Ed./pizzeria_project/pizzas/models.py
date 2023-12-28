from django.db import models

# Create your models here.
class Pizza(models.Model):
    """Class for Pizza models for our database."""
    name = models.CharField(max_length=64, blank=False)

    def __str__(self):
        """String representation for our Pizza models"""
        return self.name

class Topping(models.Model):
    """Class for Topping models connected to the Pizza models."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, blank=False)
    name = models.CharField(max_length=64, blank=False)

    def __str__(self):
        """String representation for our Topping models"""
        return self.name