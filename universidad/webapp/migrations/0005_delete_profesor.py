# Generated by Django 4.0.3 on 2022-07-14 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_delete_estudianteprofesor'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profesor',
        ),
    ]