# Generated by Django 2.1.15 on 2020-08-22 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anios',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('anio', models.TextField()),
            ],
            options={
                'db_table': 'Anios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Aportesiglesias',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('iglesia_id', models.IntegerField(blank=True, null=True)),
                ('anio_id', models.IntegerField(blank=True, null=True)),
                ('ene', models.FloatField(blank=True, null=True)),
                ('feb', models.FloatField(blank=True, null=True)),
                ('mar', models.FloatField(blank=True, null=True)),
                ('abr', models.FloatField(blank=True, null=True)),
                ('may', models.FloatField(blank=True, null=True)),
                ('jun', models.FloatField(blank=True, null=True)),
                ('jul', models.FloatField(blank=True, null=True)),
                ('ago', models.FloatField(blank=True, null=True)),
                ('sep', models.FloatField(blank=True, null=True)),
                ('oct', models.FloatField(blank=True, null=True)),
                ('nov', models.FloatField(blank=True, null=True)),
                ('dic', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'aportesIglesias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Aportesobreros',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('obrero_id', models.IntegerField(blank=True, null=True)),
                ('anio_id', models.IntegerField(blank=True, null=True)),
                ('ene', models.FloatField(blank=True, null=True)),
                ('feb', models.FloatField(blank=True, null=True)),
                ('mar', models.FloatField(blank=True, null=True)),
                ('abr', models.FloatField(blank=True, null=True)),
                ('may', models.FloatField(blank=True, null=True)),
                ('jun', models.FloatField(blank=True, null=True)),
                ('jul', models.FloatField(blank=True, null=True)),
                ('ago', models.FloatField(blank=True, null=True)),
                ('sep', models.FloatField(blank=True, null=True)),
                ('oct', models.FloatField(blank=True, null=True)),
                ('nov', models.FloatField(blank=True, null=True)),
                ('dic', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'aportesObreros',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Iglesias',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('iglesia', models.TextField()),
                ('provincia', models.TextField(blank=True, null=True)),
                ('presbiterio', models.TextField(blank=True, null=True)),
                ('alta', models.TextField(blank=True, null=True)),
                ('baja', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Iglesias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Obreros',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('folio', models.TextField(blank=True, null=True)),
                ('nombre', models.TextField(blank=True, db_column='Nombre', null=True)),
                ('alta', models.TextField(blank=True, null=True)),
                ('baja', models.TextField(blank=True, null=True)),
                ('iglesia_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Obreros',
                'managed': False,
            },
        ),
    ]
