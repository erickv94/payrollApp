# Generated by Django 3.0.5 on 2020-05-03 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0001_initial'),
        ('usuario', '0002_auto_20200502_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='empleado',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='empleado.Empleado'),
        ),
    ]
