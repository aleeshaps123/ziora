# Generated by Django 4.2.5 on 2024-04-15 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saree', '0003_order_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(default='Uncategorized', max_length=100),
        ),
    ]
