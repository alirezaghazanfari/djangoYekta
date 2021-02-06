# Generated by Django 3.1.6 on 2021-02-06 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Advertiser_management', '0004_auto_20210131_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='click',
            name='ad',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='click_ad', to='Advertiser_management.ad'),
        ),
        migrations.AlterField(
            model_name='view',
            name='ad',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='view_ad', to='Advertiser_management.ad'),
        ),
    ]