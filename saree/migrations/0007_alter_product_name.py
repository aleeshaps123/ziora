# Generated by Django 4.2.5 on 2024-05-19 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saree', '0006_alter_userprofile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
