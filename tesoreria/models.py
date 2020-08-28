# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.utils.html import format_html
from datetime import datetime

from django.db import models

class Anios(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    anio = models.TextField(max_length=10)

    class Meta:
        managed = True
        db_table = 'Anios'

    def __str__(self):
        return self.anio


class Iglesias(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    iglesia = models.CharField(max_length=200)
    provincia = models.CharField(blank=True, null=True,max_length=200)
    presbiterio = models.CharField(blank=True, null=True,max_length=200)
    alta = models.DateField(blank=True, null=True)
    baja = models.DateField(blank=True, null=True)
    activa = models.BooleanField(default=True)
    misioneros = models.ManyToManyField('Obreros', blank=True, verbose_name="Es obrero en")

    def __str__(self):
        return self.iglesia

    class Meta:
        managed = True
        db_table = 'Iglesias'
        verbose_name_plural = "Iglesias y misiones"
        verbose_name = "Iglesia"


class Obreros(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    foto = models.ImageField(upload_to="tesoreria/avatars", null=True, blank=True, default='static/assets/img/theme/team-1-800x800.jpg')
    folio = models.CharField(blank=True, null=True,max_length=20)
    nombre = models.CharField(db_column='Nombre', blank=True, null=True,max_length=200)  # Field name made lowercase.
    alta = models.DateField(blank=True, null=True)
    baja = models.DateField(blank=True, null=True)
    iglesia_id = models.ManyToManyField("Iglesias", through=Iglesias.misioneros.through, blank=True, verbose_name="Iglesias donde ministra" )
    activo = models.BooleanField(default=True)



    def __str__(self):
        return self.nombre

    class Meta:
        managed = True
        db_table = 'Obreros'
        verbose_name_plural = "Pastores y obreros"
        verbose_name = "Pastor"


class Aportesiglesias(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    # por defecto lomando para encrucijada
    iglesia_id = models.ForeignKey("Iglesias", on_delete=models.CASCADE, blank=False, null=False,
                                   verbose_name='Iglesia que aporta',
                                   default=Iglesias.objects.get(iglesia='ENCRUCIJADA').id)
    anio_id = models.ForeignKey("Anios", on_delete=models.DO_NOTHING, blank=False, null=False,
                                default=Anios.objects.get(anio=str(datetime.now().year)).id,verbose_name="año")
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
        verbose_name_plural = "Aportes de iglesias"
        verbose_name = "Aporte de iglesia"

    # def iglesian(self):
    #     return self.iglesia_id
    #
    # def anion(self):
    #     self.anio_id
    def total(self):
        t = self.ene + self.feb + self.mar + self.abr + self.may + self.jun + self.jul + self.ago + self.sep + self.oct + self.nov + self.dic
        return '$ %.2f' % t

    def __str__(self):
        return '%s-%s' % (self.iglesia_id.iglesia, self.anio_id.anio)


class Aportesobreros(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?

    obrero_id = models.ForeignKey("Obreros", on_delete=models.CASCADE, blank=False, null=False,
                                  verbose_name='Obrero que aporta', default='')
    anio_id = models.ForeignKey("Anios", on_delete=models.DO_NOTHING, blank=False, null=False,
                                default=Anios.objects.get(anio=str(datetime.now().year)).id,verbose_name="año")

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
        verbose_name_plural = "Aportes de obreros"
        verbose_name = "Aporte de obrero"


    def __str__(self):
        return '%s-%s' % (self.obrero_id.nombre, self.anio_id.anio)

    def total(self):
        t = self.ene + self.feb + self.mar + self.abr + self.may + self.jun + self.jul + self.ago + self.sep + self.oct + self.nov + self.dic
        return '$ %.2f' % t