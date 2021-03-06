# Generated by Django 2.1.15 on 2020-06-14 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('sociedad', models.CharField(max_length=100, null=True)),
                ('representante_legal', models.CharField(max_length=100, null=True)),
                ('descripcion', models.CharField(max_length=200, null=True)),
                ('telefono', models.CharField(max_length=10, null=True)),
                ('web', models.CharField(max_length=50, null=True)),
                ('nic', models.CharField(max_length=20, null=True)),
                ('nit', models.CharField(max_length=20, null=True)),
                ('direccion', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('salario_minimo_sector', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            options={
                'db_table': 'configuracion',
            },
        ),
    ]
