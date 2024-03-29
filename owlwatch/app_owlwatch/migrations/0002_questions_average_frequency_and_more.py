# Generated by Django 5.0.1 on 2024-01-14 11:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_owlwatch', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='average_frequency',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questions',
            name='average_intensity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questions',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
