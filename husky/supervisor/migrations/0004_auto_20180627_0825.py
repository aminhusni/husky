# Generated by Django 2.0.6 on 2018-06-27 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supervisor', '0003_auto_20180626_0320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check_item',
            name='dustbin',
            field=models.BooleanField(default=False, verbose_name='Dustbin'),
        ),
        migrations.AlterField(
            model_name='check_item',
            name='floor',
            field=models.BooleanField(default=False, verbose_name='Floor'),
        ),
        migrations.AlterField(
            model_name='check_item',
            name='handsoap',
            field=models.BooleanField(default=False, verbose_name='Handsoap'),
        ),
        migrations.AlterField(
            model_name='check_item',
            name='mirror',
            field=models.BooleanField(default=False, verbose_name='Mirror'),
        ),
        migrations.AlterField(
            model_name='check_item',
            name='smell',
            field=models.BooleanField(default=False, verbose_name='Smell'),
        ),
        migrations.AlterField(
            model_name='check_item',
            name='tissue',
            field=models.BooleanField(default=False, verbose_name='Tissue'),
        ),
        migrations.AlterField(
            model_name='check_item',
            name='toilet_bowl',
            field=models.BooleanField(default=False, verbose_name='Toilet bowl'),
        ),
        migrations.AlterField(
            model_name='check_item',
            name='urinal_bowl',
            field=models.BooleanField(default=False, verbose_name='Urinal bowl'),
        ),
        migrations.AlterField(
            model_name='check_item',
            name='wall',
            field=models.BooleanField(default=False, verbose_name='Wall'),
        ),
        migrations.AlterField(
            model_name='check_item',
            name='wash_basin',
            field=models.BooleanField(default=False, verbose_name='Wash basin'),
        ),
    ]
