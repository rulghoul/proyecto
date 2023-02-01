# Generated by Django 4.1.3 on 2023-01-20 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salones', '0014_alter_tipoevento_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encevento',
            name='opcion',
            field=models.PositiveSmallIntegerField(blank=True, db_column='Opcion', null=True),
        ),
        migrations.AlterField(
            model_name='historicalencevento',
            name='opcion',
            field=models.PositiveSmallIntegerField(blank=True, db_column='Opcion', null=True),
        ),
        migrations.AlterField(
            model_name='tipoevento',
            name='descripcion',
            field=models.CharField(db_column='DescTipoEvento', max_length=50),
        ),
    ]