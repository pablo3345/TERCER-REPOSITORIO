# Generated by Django 5.0.6 on 2024-06-24 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoryproduct',
            name='Measure_Unit',
        ),
        migrations.RemoveField(
            model_name='historicalcategoryproduct',
            name='Measure_Unit',
        ),
    ]
