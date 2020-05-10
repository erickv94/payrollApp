# Generated by Django 3.0.5 on 2020-05-10 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImpuestoRenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porcentaje', models.IntegerField()),
                ('minimo', models.DecimalField(decimal_places=2, max_digits=8)),
                ('maximo', models.DecimalField(decimal_places=2, max_digits=8)),
                ('exceso', models.DecimalField(decimal_places=2, max_digits=8)),
                ('cuota_fija', models.DecimalField(decimal_places=2, max_digits=8)),
                ('tramo', models.CharField(max_length=100)),
                ('periocidad', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'impuesto_renta',
            },
        ),
    ]
