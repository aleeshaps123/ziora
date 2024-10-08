# Generated by Django 5.0.1 on 2024-05-19 20:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saree', '0009_remove_seller_address_remove_seller_phone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('order_status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=10)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saree.product')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saree.seller')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saree.supplier')),
            ],
        ),
    ]
