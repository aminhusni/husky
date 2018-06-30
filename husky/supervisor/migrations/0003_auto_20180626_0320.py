# Generated by Django 2.0.6 on 2018-06-26 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supervisor', '0002_auto_20180625_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supervisor',
            name='supervisor_type',
            field=models.CharField(choices=[('CL', 'Cleaner'), ('AD', 'Admin')], default='CL', max_length=2),
        ),
    ]