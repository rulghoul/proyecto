# Generated by Django 4.1.3 on 2022-12-09 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    #replaces = [('salones', '0001_rename_cvetipoactividad_tipoactividad_clave_and_more'), ('salones', '0005_alter_tipoactividad_bandactivo_and_more')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoActividad',
            fields=[
                ('id_pk', models.SmallAutoField(db_column='IdTipoActividad', primary_key=True, serialize=False)),
                ('clave', models.CharField(db_column='CveTipoActividad', max_length=20, verbose_name='Clave')),
                ('descripcion', models.CharField(db_column='DescTipoActividad', max_length=50, verbose_name='Descripcion')),
                ('bandactivo', models.BooleanField(db_column='BandActivo', default=True, verbose_name='Activo')),
            ],
            options={
                'db_table': 'TIPO_ACTIVIDAD',
            },
        ),
        migrations.CreateModel(
            name='TipoEvento',
            fields=[
                ('id_pk', models.SmallAutoField(db_column='IdTipoEvento', primary_key=True, serialize=False)),
                ('clave', models.CharField(db_column='CveTipoEvento', help_text='La clave que se mostrara en menus', max_length=20, verbose_name='Clave')),
                ('descripcion', models.CharField(db_column='DescTipoEvento', max_length=50, verbose_name='Descripcion')),
                ('bandactivo', models.BooleanField(db_column='BandActivo', default=True, verbose_name='Activo')),
            ],
            options={
                'db_table': 'TIPO_EVENTO',
            },
        ),
        migrations.CreateModel(
            name='TipoServicio',
            fields=[
                ('id_pk', models.SmallAutoField(db_column='IdTipoServicio', primary_key=True, serialize=False)),
                ('clave', models.CharField(db_column='CveTipoServicio', max_length=20, verbose_name='Clave')),
                ('descripcion', models.CharField(db_column='DescServicio', max_length=50, verbose_name='Descripcion')),
                ('bandactivo', models.BooleanField(db_column='BandActivo', default=True, verbose_name='Activo')),
            ],
            options={
                'db_table': 'TIPO_SERVICIO',
            },
        ),
    ]
