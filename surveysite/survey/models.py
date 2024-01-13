from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

NUMBER_CHOICES = (
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)


# Create your models here.
class Questions(models.Model):
    """Survey form model for stroring questions and answers in our database."""

    question1_1 = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question1_2 = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question2_1 = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question2_2 = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )
