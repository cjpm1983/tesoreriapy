# Generated by Django 2.1.15 on 2020-08-22 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0012_auto_20200822_0233'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='activo',
            field=models.BooleanField(default=False, verbose_name='Curso Activo'),
        ),
    ]