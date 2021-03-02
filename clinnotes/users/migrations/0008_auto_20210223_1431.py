# Generated by Django 3.0.12 on 2021-02-23 14:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210223_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='episodeofcare',
            name='discharge_date',
            field=models.DateTimeField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='next_appointment',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
    ]
