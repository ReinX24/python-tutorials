from django.db import models

from django.conf import settings
from django.utils import timezone


# Create your models here.
class Entry(models.Model):
    """Entry model where the user can store their journal entries."""

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """String representation of our entry model."""
        return self.title
