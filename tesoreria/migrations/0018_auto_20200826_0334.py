# Generated by Django 2.1.15 on 2020-08-26 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tesoreria', '0017_auto_20200823_1352'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aportesiglesias',
            options={'managed': True, 'verbose_name': 'Aporte de iglesia', 'verbose_name_plural': 'Aportes de iglesias'},
        ),
        migrations.AlterModelOptions(
            name='aportesobreros',
            options={'managed': True, 'verbose_name': 'Aporte de obrero', 'verbose_name_plural': 'Aportes de obreros'},
        ),
        migrations.AlterModelOptions(
            name='iglesias',
            options={'managed': True, 'verbose_name': 'Iglesia', 'verbose_name_plural': 'Iglesias y misiones'},
        ),
        migrations.AlterModelOptions(
            name='obreros',
            options={'managed': True, 'verbose_name': 'Pastor', 'verbose_name_plural': 'Pastores y obreros'},
        ),
        migrations.AlterField(
            model_name='aportesiglesias',
            name='anio_id',
            field=models.ForeignKey(default=38, on_delete=django.db.models.deletion.DO_NOTHING, to='tesoreria.Anios', verbose_name='año'),
        ),
        migrations.AlterField(
            model_name='aportesobreros',
            name='anio_id',
            field=models.ForeignKey(default=38, on_delete=django.db.models.deletion.DO_NOTHING, to='tesoreria.Anios', verbose_name='año'),
        ),
    ]
