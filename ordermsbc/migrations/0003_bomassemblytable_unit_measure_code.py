# Generated by Django 4.1.3 on 2022-11-24 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordermsbc', '0002_delete_bomtable'),
    ]

    operations = [
        migrations.AddField(
            model_name='bomassemblytable',
            name='unit_measure_code',
            field=models.CharField(default='', max_length=25),
        ),
    ]
