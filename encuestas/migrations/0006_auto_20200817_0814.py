# Generated by Django 2.1.15 on 2020-08-17 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0005_auto_20200817_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(null=True, upload_to='encuestas/avatars'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='background',
            field=models.ImageField(null=True, upload_to='encuestas/avatars_bg'),
        ),
    ]
