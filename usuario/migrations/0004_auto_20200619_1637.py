# Generated by Django 2.1.15 on 2020-06-19 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_auto_20200619_1622'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='sub_menu',
            new_name='padre',
        ),
    ]
