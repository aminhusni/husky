# Generated by Django 2.0.6 on 2018-06-29 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supervisor', '0004_auto_20180627_0825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checklist',
            name='supervisor_type',
        ),
        migrations.AlterField(
            model_name='checklist',
            name='employee_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supervisor.Supervisor'),
        ),
    ]