# Generated by Django 4.1.3 on 2022-11-12 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_alter_order_file_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ship_by',
            field=models.CharField(default='', max_length=10),
        ),
    ]
