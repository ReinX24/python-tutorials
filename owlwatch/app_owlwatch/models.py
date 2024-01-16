from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

NUMBER_CHOICES = (
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)


# Create your models here.
class Averages(models.Model):
    """Averages model for storing average_intensity and average_frequency."""

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    average_intensity = models.FloatField(default=0)
    average_frequency = models.FloatField(default=0)


class Questions(models.Model):
    """Survey form model for stroring questions and answers in our database."""

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    question1_intensity = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question1_frequency = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question2_intensity = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question2_frequency = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )
