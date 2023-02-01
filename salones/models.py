# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True44
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from simple_history.models import HistoricalRecords

class ClasifServicio(models.Model):
    idclasifservicio = models.SmallAutoField(db_column='IdClasifServicio', primary_key=True)  # Field name made lowercase.
    cvetiposervicio = models.ForeignKey('TipoServicio', models.DO_NOTHING, db_column='CveTipoServicio')  # Field name made lowercase.
    cveclasifservicio = models.CharField(db_column='CveClasifServicio', unique=True, max_length=20)  # Field name made lowercase.
    descclasifservicio = models.CharField(db_column='DescClasifServicio', unique=True, max_length=50)  # Field name made lowercase.
    bandactivo = models.BooleanField(db_column='BandActivo', blank=False, null=False, default=True, verbose_name='Activo')  # Field name made lowercase.

    class Meta:
        db_table = 'clasif_servicio'


class DesgloseServicio(models.Model):
    iddesgloseservicio = models.SmallAutoField(db_column='IdDesgloseServicio', primary_key=True)  # Field name made lowercase.
    cveclasifservicio = models.ForeignKey(ClasifServicio, models.DO_NOTHING, db_column='CveClasifServicio')  # Field name made lowercase.
    cvedesgloseservicio = models.CharField(db_column='CveDesgloseServicio', unique=True, max_length=20)  # Field name made lowercase.
    descdesgloseservicio = models.CharField(db_column='DescDesgloseServicio', unique=True, max_length=50)  # Field name made lowercase.
    bandactivo = models.BooleanField(db_column='BandActivo', blank=False, null=False, default=True, verbose_name='Activo')  # Field name made lowercase.
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate')  # Field name made lowercase.
    
    class Meta:
        db_table = 'desglose_servicio'



class EstatusActividad(models.Model):
    idestatusactividad = models.SmallAutoField(db_column='IdEstatusActividad', primary_key=True)  # Field name made lowercase.
    clave = models.CharField(db_column='CveEstatusActividad', unique=True, max_length=20)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DescEstatusActividad', unique=True, max_length=50)  # Field name made lowercase.
    bandactivo = models.BooleanField(db_column='BandActivo', blank=False, null=False, default=True, verbose_name='Activo')  # Field name made lowercase.

    def __str__(self) -> str:
        return self.clave

    class Meta:
        db_table = 'estatus_actividad'


class FasesProcesos(models.Model):
    idfase = models.SmallAutoField(db_column='IdFase', primary_key=True)  # Field name made lowercase.
    #cveproceso = models.ForeignKey('Procesos', models.DO_NOTHING, db_column='CveProceso')  # Field name made lowercase.
    cvefase = models.CharField(db_column='CveFase', unique=True, max_length=20)  # Field name made lowercase.
    descfase = models.CharField(db_column='DescFase', unique=True, max_length=50)  # Field name made lowercase.
    bandactivo = models.BooleanField(db_column='BandActivo', blank=False, null=False, default=True, verbose_name='Activo')  # Field name made lowercase.

    class Meta:
        db_table = 'fases_procesos'




class TipoPersona(models.Model):
    id_pk = models.SmallAutoField(db_column='IdTipoPersona', primary_key=True)  # Field name made lowercase.
    clave = models.CharField(db_column='CveTipoPersona', unique=True, max_length=20, verbose_name='Clave')  # Field name made lowercase.
    descripcion = models.CharField(db_column='DescTipoPersona', unique=True, max_length=50, verbose_name='Descripcion')  # Field name made lowercase.
    bandactivo = models.BooleanField(db_column='BandActivo', blank=False, null=False, default=True, verbose_name='Activo')  # Field name made lowercase.

    def __str__(self) -> str:
        return self.descripcion

    class Meta:
        db_table = 'TIPO_PERSONA'



class PersonaPrincipal(models.Model):
    idpersonaprincipal = models.SmallAutoField(db_column='IdPersonaPrincipal', primary_key=True)  # Field name made lowercase.
    cvetipopersona = models.ForeignKey(TipoPersona, models.DO_NOTHING, db_column='CveTipoPersona')  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100)  # Field name made lowercase.
    primer_apellido = models.CharField(db_column='Primer_Apellido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    segundo_apellido = models.CharField(db_column='Segundo_Apellido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    correo = models.EmailField(db_column='Correo', max_length=70)  # Field name made lowercase.
    telefono1 = models.CharField(db_column='Telefono1', max_length=50)  # Field name made lowercase.
    telefono2 = models.CharField(db_column='Telefono2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datestar = models.DateTimeField(db_column='DateStar',auto_now_add=True)  # Field name made lowercase.
    bandactivo = models.BooleanField(db_column='BandActivo', blank=False, null=False, default=True, verbose_name='Activo')  # Field name made lowercase.

    def __str__(self) -> str:
        return f"{self.nombre} {self.primer_apellido} {self.segundo_apellido}"

    class Meta:
        db_table = 'persona_principal'


class Procesos(models.Model):
    id_pk = models.SmallAutoField(db_column='IdProceso', primary_key=True)  # Field name made lowercase.
    clave = models.CharField(db_column='CveProceso', unique=True, max_length=20)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DescProceso', unique=True, max_length=50)  # Field name made lowercase.
    bandactivo = models.BooleanField(db_column='BandActivo', blank=False, null=False, default=True, verbose_name='Activo')  # Field name made lowercase.

    def __str__(self) -> str:
        return self.clave

    class Meta:
        db_table = 'procesos'


class SeguimientoEvento(models.Model):
    folioevento = models.PositiveSmallIntegerField(db_column='FolioEvento', primary_key=True)  # Field name made lowercase.
    cvetipopersona = models.CharField(db_column='CveTipoPersona', max_length=20)  # Field name made lowercase.
    cvepersona = models.CharField(db_column='CvePersona', max_length=20)  # Field name made lowercase.
    cvetipoevento = models.CharField(db_column='CveTipoEvento', max_length=20)  # Field name made lowercase.
    cveproceso = models.CharField(db_column='CveProceso', max_length=20)  # Field name made lowercase.
    cvefase = models.CharField(db_column='CveFase', max_length=20)  # Field name made lowercase.
    history = HistoricalRecords()

    class Meta:
        db_table = 'SEGUIMIENTO_EVENTO'


class TipoActividad(models.Model):
    id_pk = models.SmallAutoField(db_column='IdTipoActividad', primary_key=True)  # Field name made lowercase.
    clave = models.CharField(db_column='CveTipoActividad', max_length=20)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DescTipoActividad', max_length=50)  # Field name made lowercase.
    bandactivo = models.BooleanField(db_column='BandActivo', blank=False, null=False, default=True, verbose_name='Activo')  # Field name made lowercase.

    def __str__(self) -> str:
        return self.descripcion

    class Meta:
        db_table = 'TIPO_ACTIVIDAD'


class TipoEvento(models.Model):
    id_pk = models.SmallAutoField(db_column='IdTipoEvento', primary_key=True)  # Field name made lowercase.
    clave = models.CharField(db_column='CveTipoEvento', unique=True, max_length=20)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DescTipoEvento', unique=False, max_length=50)  # Field name made lowercase.
    bandactivo = models.BooleanField(db_column='BandActivo', blank=False, null=False, default=True, verbose_name='Activo')  # Field name made lowercase.

    def __str__(self) -> str:
        return self.descripcion

    class Meta:
        db_table = 'TIPO_EVENTO'


class TipoServicio(models.Model):
    id_pk = models.SmallAutoField(db_column='IdTipoServicio', primary_key=True)  # Field name made lowercase.
    clave = models.CharField(db_column='CveTipoServicio', unique=True, max_length=20, verbose_name='Clave')  # Field name made lowercase.
    descripcion = models.CharField(db_column='DescServicio', max_length=50, verbose_name='Descripcion')  # Field name made lowercase.
    bandactivo = models.BooleanField(db_column='BandActivo', blank=False, null=False, default=True, verbose_name='Activo')  # Field name made lowercase.

    def __str__(self) -> str:
        return self.descripcion

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


class EncEvento(models.Model):
    folioevento = models.SmallAutoField(db_column='FolioEvento', primary_key=True)  # Field name made lowercase.
    cvetipoevento = models.ForeignKey(TipoEvento, models.DO_NOTHING, db_column='CveTipoEvento')  # Field name made lowercase.
    cvepersona = models.ForeignKey(PersonaPrincipal, models.DO_NOTHING, db_column='CvePersona')  # Field name made lowercase.
    opcion = models.PositiveSmallIntegerField(db_column='Opcion', blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    banaprovada = models.BooleanField(db_column='BanAprovada', blank=False, null=False, default=True, verbose_name='Aprobada')  # Field name made lowercase.
    history = HistoricalRecords()

    class Meta:
        db_table = 'enc_evento'



class EncEventoOpcion(models.Model):
    folioevento = models.PositiveSmallIntegerField(db_column='FolioEvento', primary_key=True)  # Field name made lowercase.
    evento = models.PositiveSmallIntegerField(db_column='CveEvento')  # Field name made lowercase.
    persona = models.PositiveSmallIntegerField(db_column='CvePersona')  # Field name made lowercase.
    numopcion = models.PositiveSmallIntegerField(db_column='NumOpcion', blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    monto = models.FloatField(db_column='Monto', blank=True, null=True)  # Field name made lowercase.
    history = HistoricalRecords()

    def __str__(self) -> str:
        return self.nombre


    class Meta:
        db_table = 'enc_evento_opcion'


class DetEvento(models.Model):
    iddetalle = models.PositiveSmallIntegerField(db_column='IdDetalle', primary_key=True)  # Field name made lowercase.
    cveopcion = models.ForeignKey('EncEventoOpcion', models.DO_NOTHING, db_column='CveOpcion')  # Field name made lowercase.
    cvetipoactividad = models.ForeignKey('TipoActividad', models.DO_NOTHING, db_column='CveTipoActividad')  # Field name made lowercase.
    cvedesgloseservicio = models.ForeignKey(DesgloseServicio, models.DO_NOTHING, db_column='CveDesgloseServicio')  # Field name made lowercase.
    cveclasifservicio = models.ForeignKey(ClasifServicio, models.DO_NOTHING, db_column='CveClasifServicio')  # Field name made lowercase.
    cvetiposervicio = models.ForeignKey('TipoServicio', models.DO_NOTHING, db_column='CveTipoServicio')  # Field name made lowercase.
    costo = models.FloatField(db_column='Costo', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    history = HistoricalRecords()

    class Meta:
        db_table = 'det_evento'



class Egresos(models.Model):
    id_egresos = models.SmallAutoField(primary_key=True)
    cve_detalle = models.ForeignKey(DetEvento, models.DO_NOTHING, db_column='Cve_detalle')  # Field name made lowercase.
    monto = models.FloatField(db_column='Monto')  # Field name made lowercase.
    spei = models.CharField(db_column='SPEI', max_length=50)  # Field name made lowercase.
    history = HistoricalRecords()

    class Meta:
        db_table = 'egresos'

class Ingresos(models.Model):
    idingresos = models.OneToOneField(EncEvento, models.DO_NOTHING, db_column='IdIngresos', primary_key=True)  # Field name made lowercase.
    cveevento = models.PositiveSmallIntegerField(db_column='CveEvento')  # Field name made lowercase.
    monto = models.FloatField(db_column='Monto')  # Field name made lowercase.
    spei = models.CharField(db_column='SPEI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    history = HistoricalRecords()

    class Meta:
        db_table = 'ingresos'

