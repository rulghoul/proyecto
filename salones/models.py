from django.db import models
class TipoActividad(models.Model):
    id_pk = models.SmallAutoField(db_column='IdTipoActividad', primary_key=True)  # Field name made lowercase.
    clave = models.CharField(db_column='CveTipoActividad', max_length=20,  verbose_name='Clave')  # Field name made lowercase.
    descripcion = models.CharField(db_column='DescTipoActividad', max_length=50, verbose_name='Descripcion')  # Field name made lowercase.
    bandactivo = models.BooleanField(db_column='BandActivo', blank=False, null=False, default=True, verbose_name='Activo')  # Field name made lowercase.

    def __str__(self) -> str:
        return self.clave

    class Meta:
        db_table = 'TIPO_ACTIVIDAD'


class TipoEvento(models.Model):
    id_pk = models.SmallAutoField(db_column='IdTipoEvento', primary_key=True)  # Field name made lowercase.
    clave = models.CharField(db_column='CveTipoEvento', max_length=20,  verbose_name='Clave', help_text='La clave que se mostrara en menus')  # Field name made lowercase.
    descripcion = models.CharField(db_column='DescTipoEvento', max_length=50, verbose_name='Descripcion')  # Field name made lowercase.
    bandactivo = models.BooleanField(db_column='BandActivo', blank=False, null=False, default=True, verbose_name='Activo')  # Field name made lowercase.

    def __str__(self) -> str:
        return self.clave

    class Meta:
        db_table = 'TIPO_EVENTO'


class TipoServicio(models.Model):
    id_pk = models.SmallAutoField(db_column='IdTipoServicio', primary_key=True)  # Field name made lowercase.
    clave = models.CharField(db_column='CveTipoServicio', max_length=20,  verbose_name='Clave')  # Field name made lowercase.
    descripcion = models.CharField(db_column='DescServicio', max_length=50, verbose_name='Descripcion')  # Field name made lowercase.
    bandactivo = models.BooleanField(db_column='BandActivo', blank=False, null=False, default=True, verbose_name='Activo')  # Field name made lowercase.

    def __str__(self) -> str:
        return self.clave

    class Meta:
        db_table = 'TIPO_SERVICIO'


class Foto(models.Model):
    title = models.CharField(max_length=60, default='', blank=True)
    description = models.TextField(max_length=200, default='', blank=True)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(width_field="width", height_field="height")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["timestamp"]
        verbose_name = 'Foto'