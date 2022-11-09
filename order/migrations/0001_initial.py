# Generated by Django 4.1.3 on 2022-11-04 11:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterDocs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='MasterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Particular', models.CharField(default='', max_length=50)),
                ('Ordered_ItemCode', models.CharField(default='', max_length=20)),
                ('Base_ItemCode', models.CharField(default='', max_length=20)),
                ('Qty', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(default='', max_length=10)),
                ('particular', models.CharField(default='', max_length=50)),
                ('itemcode', models.CharField(default='', max_length=10)),
                ('base_item_code', models.CharField(default='', max_length=10)),
                ('qty', models.CharField(default='', max_length=10)),
                ('cust', models.CharField(default='', max_length=10)),
                ('address', models.CharField(default='', max_length=50)),
                ('ship_by', models.CharField(default='RAM', max_length=10)),
                ('consignee', models.CharField(default='', max_length=10)),
                ('country', models.CharField(default='', max_length=10)),
                ('phone', models.CharField(default='', max_length=20)),
                ('pincode', models.CharField(default='', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Docs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='')),
                ('customer_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]