# Generated by Django 3.1.3 on 2020-11-20 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimes', '0004_auto_20201120_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departments',
            name='latitude',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='departments',
            name='longitude',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
