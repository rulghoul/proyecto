# Generated by Django 4.1.3 on 2022-12-02 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salones', '0003_alter_tipoactividad_bandactivo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tipoactividad',
            old_name='cvetipoactividad',
            new_name='clave',
        ),
        migrations.RenameField(
            model_name='tipoactividad',
            old_name='desctipoactividad',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='tipoactividad',
            old_name='idtipoactividad',
            new_name='id_pk',
        ),
        migrations.RenameField(
            model_name='tipoevento',
            old_name='cvetipoevento',
            new_name='clave',
        ),
        migrations.RenameField(
            model_name='tipoevento',
            old_name='desctipoevento',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='tipoevento',
            old_name='idtipoevento',
            new_name='id_pk',
        ),
        migrations.RenameField(
            model_name='tiposervicio',
            old_name='cvetiposervicio',
            new_name='clave',
        ),
        migrations.RenameField(
            model_name='tiposervicio',
            old_name='descservicio',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='tiposervicio',
            old_name='idtiposervicio',
            new_name='id_pk',
        ),
    ]
