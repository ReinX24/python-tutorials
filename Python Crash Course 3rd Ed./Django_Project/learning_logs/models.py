from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about to be stored in a database."""

    text = models.CharField(max_length=256)
    date_added = models.DateTimeField(auto_now_add=True)
    # Making each Topic be connected to their own user, this means that when 
    # the user is deleted, all related Topic objects to that user are also 
    # deleted from the database.
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """An entry that contains information abou a topic."""

    # A ForeignKey is an attribute that comes from another class or in this
    # case, a record in our Topic database. on_delete=models.CASCADE means that
    # when the associated key or Topic is deleted, all entries related to that
    # key will also be deleted.
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Tells Django to use 'entries' when refering to more that one entry.
        """

        verbose_name_plural = "entries"

    def __str__(self):
        """Return a simple string representing the entry."""
        # 18 - 2 Short Entries
        if len(self.text) <= 50:
            return f"{self.text}"
        return f"{self.text[:50]}..."  # returns first 50 characters
