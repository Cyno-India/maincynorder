# Generated by Django 4.1.3 on 2022-11-24 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordermsbc', '0003_bomassemblytable_unit_measure_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemcard',
            name='Sales_Unit_of_Measure',
            field=models.CharField(default='', max_length=25),
        ),
    ]
