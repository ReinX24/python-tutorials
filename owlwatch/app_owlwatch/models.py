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
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
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

    question3_intensity = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question3_frequency = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question4_intensity = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question4_frequency = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question5_intensity = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question5_frequency = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question6_intensity = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question6_frequency = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question7_intensity = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question7_frequency = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question8_intensity = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question8_frequency = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question9_intensity = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question9_frequency = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question10_intensity = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question10_frequency = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question11_intensity = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question11_frequency = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question12_intensity = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question12_frequency = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question13_intensity = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question13_frequency = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question14_intensity = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question14_frequency = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question15_intensity = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question15_frequency = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question16_intensity = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question16_frequency = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question17_intensity = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    question17_frequency = models.IntegerField(
        default=0,
        choices=NUMBER_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )
