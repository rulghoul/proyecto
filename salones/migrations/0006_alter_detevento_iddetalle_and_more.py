# Generated by Django 4.1.3 on 2023-02-12 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("salones", "0005_detevento_opcion_historicaldetevento_opcion_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="detevento",
            name="iddetalle",
            field=models.SmallAutoField(
                db_column="IdDetalle", primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="historicaldetevento",
            name="iddetalle",
            field=models.IntegerField(blank=True, db_column="IdDetalle", db_index=True),
        ),
    ]
