# Generated by Django 4.1.3 on 2022-12-09 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordermsbc', '0005_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemcard',
            name='Net_Weight',
            field=models.CharField(default='', max_length=25),
        ),
    ]