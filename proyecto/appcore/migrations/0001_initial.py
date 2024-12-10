# Generated by Django 5.1.4 on 2024-12-07 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=40)),
                ('nombre', models.CharField(max_length=100)),
                ('duracion', models.CharField(max_length=40)),
                ('genero', models.CharField(max_length=40)),
                ('calificacion', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=40)),
                ('nombre', models.CharField(max_length=100)),
                ('duracion', models.CharField(max_length=40)),
                ('genero', models.CharField(max_length=40)),
                ('calificacion', models.CharField(max_length=40)),
            ],
        ),
    ]