# Generated by Django 4.1.3 on 2023-02-01 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salones', '0016_rename_cveevento_enceventoopcion_evento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='detevento',
            name='tiempo',
            field=models.PositiveSmallIntegerField(db_column='Tiempo', default=None, null=True),
        ),
        migrations.AddField(
            model_name='historicaldetevento',
            name='tiempo',
            field=models.PositiveSmallIntegerField(db_column='Tiempo', default=None, null=True),
        ),
    ]