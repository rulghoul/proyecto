# Generated by Django 4.1.3 on 2023-01-11 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salones', '0012_alter_personaprincipal_datestar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaprincipal',
            name='cvetipopersona',
            field=models.ForeignKey(db_column='CveTipoPersona', on_delete=django.db.models.deletion.DO_NOTHING, to='salones.tipopersona'),
        ),
    ]