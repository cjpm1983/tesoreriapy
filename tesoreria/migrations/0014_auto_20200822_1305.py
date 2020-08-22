# Generated by Django 2.1.15 on 2020-08-22 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tesoreria', '0013_obreros_activo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anios',
            name='anio',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='iglesias',
            name='iglesia',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='iglesias',
            name='misioneros',
            field=models.ManyToManyField(blank=True, to='tesoreria.Obreros', verbose_name='Es obrero en'),
        ),
        migrations.AlterField(
            model_name='iglesias',
            name='presbiterio',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='iglesias',
            name='provincia',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='obreros',
            name='folio',
            field=models.TextField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='obreros',
            name='iglesia_id',
            field=models.ManyToManyField(blank=True, to='tesoreria.Iglesias', verbose_name='Iglesias donde ministra'),
        ),
        migrations.AlterField(
            model_name='obreros',
            name='nombre',
            field=models.TextField(blank=True, db_column='Nombre', max_length=200, null=True),
        ),
    ]
