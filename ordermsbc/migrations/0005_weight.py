# Generated by Django 4.1.3 on 2022-12-08 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordermsbc', '0004_itemcard_sales_unit_of_measure'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Document_No', models.CharField(default='', max_length=20)),
                ('Line_No', models.CharField(default='', max_length=50)),
                ('Courier_Channel', models.CharField(default='', max_length=25)),
                ('Country', models.CharField(default='', max_length=25)),
                ('From_Weight', models.CharField(default='', max_length=25)),
                ('To_Weight', models.CharField(default='', max_length=25)),
                ('Amount', models.CharField(default='', max_length=25)),
            ],
        ),
    ]
