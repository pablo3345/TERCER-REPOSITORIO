# Generated by Django 3.0.7 on 2022-10-19 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=254)),
                ('edad', models.IntegerField()),
                ('telefono', models.CharField(max_length=40)),
                ('sexo', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=30)),
                ('codigo_postal', models.IntegerField()),
                ('mensaje', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
                'db_table': 'personas',
                'ordering': ['id'],
            },
        ),
    ]
