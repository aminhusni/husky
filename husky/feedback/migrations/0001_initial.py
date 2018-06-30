# Generated by Django 2.0.6 on 2018-06-25 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('location_id', models.TextField(max_length=100)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clogged', models.BooleanField(default=False)),
                ('toilet_paper', models.BooleanField(default=False)),
                ('lighting', models.BooleanField(default=False)),
                ('soap', models.BooleanField(default=False)),
                ('hose', models.BooleanField(default=False)),
                ('temperature', models.BooleanField(default=False)),
                ('bowl', models.BooleanField(default=False)),
                ('sink', models.BooleanField(default=False)),
                ('smell', models.BooleanField(default=False)),
                ('fault', models.BooleanField(default=False)),
                ('feedback', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.Feedback')),
            ],
        ),
    ]
