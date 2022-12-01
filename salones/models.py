from django.db import models
class TipoActividad(models.Model):
    idtipoactividad = models.SmallAutoField(db_column='IdTipoActividad', primary_key=True)  # Field name made lowercase.
    cvetipoactividad = models.CharField(db_column='CveTipoActividad', max_length=20,  verbose_name='Clave')  # Field name made lowercase.
    desctipoactividad = models.CharField(db_column='DescTipoActividad', max_length=50, verbose_name='Descripcion')  # Field name made lowercase.
    bandactivo = models.BooleanField(db_column='BandActivo', blank=True, null=True, default=True, verbose_name='Activo')  # Field name made lowercase.

    class Meta:
        db_table = 'TIPO_ACTIVIDAD'


class TipoEvento(models.Model):
    idtipoevento = models.SmallAutoField(db_column='IdTipoEvento', primary_key=True)  # Field name made lowercase.
    cvetipoevento = models.CharField(db_column='CveTipoEvento', max_length=20,  verbose_name='Clave', help_text='La clave que se mostrara en menus')  # Field name made lowercase.
    desctipoevento = models.CharField(db_column='DescTipoEvento', max_length=50, verbose_name='Descripcion')  # Field name made lowercase.
    bandactivo = models.BooleanField(db_column='BandActivo', blank=True, null=True, default=True, verbose_name='Activo')  # Field name made lowercase.

    class Meta:
        db_table = 'TIPO_EVENTO'


class TipoServicio(models.Model):
    idtiposervicio = models.SmallAutoField(db_column='IdTipoServicio', primary_key=True)  # Field name made lowercase.
    cvetiposervicio = models.CharField(db_column='CveTipoServicio', max_length=20,  verbose_name='Clave')  # Field name made lowercase.
    descservicio = models.CharField(db_column='DescServicio', max_length=50, verbose_name='Descripcion')  # Field name made lowercase.
    bandactivo = models.BooleanField(db_column='BandActivo', blank=True, null=True, default=True, verbose_name='Activo')  # Field name made lowercase.

    class Meta:
        db_table = 'TIPO_SERVICIO'
