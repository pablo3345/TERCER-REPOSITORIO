# Generated by Django 3.2.19 on 2023-05-16 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personas',
            name='precio_semana',
            field=models.FloatField(null=True),
        ),
    ]