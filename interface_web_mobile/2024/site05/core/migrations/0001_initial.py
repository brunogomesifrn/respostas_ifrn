# Generated by Django 5.1.4 on 2024-12-06 14:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Area')),
            ],
        ),
        migrations.CreateModel(
            name='Publico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Publico')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=300, verbose_name='Titulo')),
                ('descricao', models.TextField(verbose_name='Descricao')),
                ('autor', models.CharField(max_length=200, verbose_name='Autor(es)')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.area')),
                ('publicos', models.ManyToManyField(to='core.publico')),
            ],
        ),
    ]