# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from datetime import datetime

from django.db import models


class Anios(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    anio = models.TextField()

    class Meta:
        managed = True
        db_table = 'Anios'

    def __str__(self):
        return self.anio


class Iglesias(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    iglesia = models.TextField()
    provincia = models.TextField(blank=True, null=True)
    presbiterio = models.TextField(blank=True, null=True)
    alta = models.TextField(blank=True, null=True)
    baja = models.TextField(blank=True, null=True)
    activa =models.BooleanField(default=True)



    def __str__(self):
        return self.iglesia

    class Meta:
        managed = True
        db_table = 'Iglesias'
        verbose_name_plural = "Iglesias"


class Obreros(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    folio = models.TextField(blank=True, null=True)
    nombre = models.TextField(db_column='Nombre', blank=True, null=True)  # Field name made lowercase.
    alta = models.TextField(blank=True, null=True)
    baja = models.TextField(blank=True, null=True)
    iglesia_id = models.ForeignKey("Iglesias",on_delete=models.DO_NOTHING, blank=True, null=True, )

    def __str__(self):
        return self.nombre

    class Meta:
        managed = True
        db_table = 'Obreros'
        verbose_name_plural = "Pastores y obreros"


class Aportesiglesias(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    #por defecto lomando para encrucijada
    iglesia_id = models.ForeignKey("Iglesias",on_delete=models.CASCADE, blank=False, null=False, verbose_name='Iglesia que aporta', default=Iglesias.objects.get(iglesia='ENCRUCIJADA').id)
    anio_id = models.ForeignKey("Anios",on_delete=models.DO_NOTHING, blank=False, null=False,default=Anios.objects.get(anio=str(datetime.now().year)).id)
    feb = models.FloatField(default=0.00)
    ene = models.FloatField(default=0.00)
    mar = models.FloatField(default=0.00)
    abr = models.FloatField(default=0.00)
    may = models.FloatField(default=0.00)
    jun = models.FloatField(default=0.00)
    jul = models.FloatField(default=0.00)
    ago = models.FloatField(default=0.00)
    sep = models.FloatField(default=0.00)
    oct = models.FloatField(default=0.00)
    nov = models.FloatField(default=0.00)
    dic = models.FloatField(default=0.00)

    class Meta:
        managed = True
        db_table = 'aportesIglesias'

    # def iglesian(self):
    #     return self.iglesia_id
    #
    # def anion(self):
    #     self.anio_id

    def __str__(self):
        return '%s-%s' % (self.iglesia_id.iglesia, self.anio_id.anio)



class Aportesobreros(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?

    obrero_id = models.ForeignKey("Obreros",on_delete=models.CASCADE, blank=False, null=False, verbose_name='Obrero que aporta', default='')
    anio_id = models.ForeignKey("Anios",on_delete=models.DO_NOTHING, blank=False, null=False,default=Anios.objects.get(anio=str(datetime.now().year)).id)

    feb = models.FloatField(default=0.00)
    ene = models.FloatField(default=0.00)
    mar = models.FloatField(default=0.00)
    abr = models.FloatField(default=0.00)
    may = models.FloatField(default=0.00)
    jun = models.FloatField(default=0.00)
    jul = models.FloatField(default=0.00)
    ago = models.FloatField(default=0.00)
    sep = models.FloatField(default=0.00)
    oct = models.FloatField(default=0.00)
    nov = models.FloatField(default=0.00)
    dic = models.FloatField(default=0.00)

    class Meta:
        managed = True
        db_table = 'aportesObreros'

    def __str__(self):
        return '%s-%s' % (self.obrero_id.nombre, self.anio_id.anio)
