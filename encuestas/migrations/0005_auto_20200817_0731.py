# Generated by Django 2.1.15 on 2020-08-17 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0004_auto_20200817_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='encuestas/avatars'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='background',
            field=models.ImageField(blank=True, null=True, upload_to='encuestas/avatars_bg'),
        ),
    ]