# Generated by Django 5.0.1 on 2024-01-12 12:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_alter_surveyquestions_question1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveyquestions',
            name='question1',
        ),
        migrations.AddField(
            model_name='surveyquestions',
            name='question1_1',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='surveyquestions',
            name='question1_2',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
