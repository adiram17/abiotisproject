from django.db import models
from datetime import datetime

class Abiotis(models.Model):
    SELECTION = [
        ('S0', 'S0'),
        ('S1', 'S1'),
        ('S2', 'S2'),
        ('S3', 'S3'),
        ('S4', 'S4'),
        ('S5', 'S5'),
        ('S6', 'S6'),
        ('S7', 'S7'),
    ]
    selection = models.CharField(db_column='selection', max_length=100, blank=False, choices=SELECTION, verbose_name='Seleksi')
    origin = models.TextField(db_column='origin', max_length=1000, blank=False, verbose_name='Asal')
    type = models.TextField(db_column='type', max_length=100, blank= True, null=True, verbose_name='Tipe')
    created_date = models.DateField( blank=True, default=datetime.now, verbose_name='Tanggal Laporan')
    umur_jagung_jantan = models.IntegerField(db_column='umur_jagung_jantan', blank=False, verbose_name='Umur Jagung Jantan (hst)')
    umur_jagung_betina = models.IntegerField(db_column='umur_jagung_betina', blank=False, verbose_name='Umur Jagung Betina (hst)')
    umur_panen = models.IntegerField(db_column='umur_panen', blank=False, verbose_name='Umur Panen (hst)')

    class Meta:
        db_table = 'abiotis'
        verbose_name = 'Abiotis'
        verbose_name_plural = 'Abiotis'

