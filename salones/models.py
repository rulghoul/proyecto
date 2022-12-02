from django.db import models
class TipoActividad(models.Model):
    id_pk = models.SmallAutoField(db_column='IdTipoActividad', primary_key=True)  # Field name made lowercase.
    clave = models.CharField(db_column='CveTipoActividad', max_length=20,  verbose_name='Clave')  # Field name made lowercase.
    descripcion = models.CharField(db_column='DescTipoActividad', max_length=50, verbose_name='Descripcion')  # Field name made lowercase.
    bandactivo = models.BooleanField(db_column='BandActivo', blank=True, null=True, default=True, verbose_name='Activo')  # Field name made lowercase.

    def __str__(self) -> str:
        return self.clave

    class Meta:
        db_table = 'TIPO_ACTIVIDAD'


class TipoEvento(models.Model):
    id_pk = models.SmallAutoField(db_column='IdTipoEvento', primary_key=True)  # Field name made lowercase.
    clave = models.CharField(db_column='CveTipoEvento', max_length=20,  verbose_name='Clave', help_text='La clave que se mostrara en menus')  # Field name made lowercase.
    descripcion = models.CharField(db_column='DescTipoEvento', max_length=50, verbose_name='Descripcion')  # Field name made lowercase.
    bandactivo = models.BooleanField(db_column='BandActivo', blank=True, null=True, default=True, verbose_name='Activo')  # Field name made lowercase.

    def __str__(self) -> str:
        return self.clave

    class Meta:
        db_table = 'TIPO_EVENTO'


class TipoServicio(models.Model):
    id_pk = models.SmallAutoField(db_column='IdTipoServicio', primary_key=True)  # Field name made lowercase.
    clave = models.CharField(db_column='CveTipoServicio', max_length=20,  verbose_name='Clave')  # Field name made lowercase.
    descripcion = models.CharField(db_column='DescServicio', max_length=50, verbose_name='Descripcion')  # Field name made lowercase.
    bandactivo = models.BooleanField(db_column='BandActivo', blank=True, null=True, default=True, verbose_name='Activo')  # Field name made lowercase.

    def __str__(self) -> str:
        return self.clave

    class Meta:
        db_table = 'TIPO_SERVICIO'
