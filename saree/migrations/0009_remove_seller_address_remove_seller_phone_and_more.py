# Generated by Django 5.0.1 on 2024-05-19 19:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saree', '0008_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='address',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='phone',
        ),
        migrations.AddField(
            model_name='seller',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
