# Generated by Django 5.0.1 on 2024-01-16 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_owlwatch', '0003_remove_questions_average_frequency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='averages',
            name='average_frequency',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='averages',
            name='average_intensity',
            field=models.FloatField(default=0),
        ),
    ]