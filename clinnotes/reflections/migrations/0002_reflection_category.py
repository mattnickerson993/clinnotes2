# Generated by Django 3.0.12 on 2021-02-19 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reflections', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reflection',
            name='category',
            field=models.CharField(choices=[('GE', 'General'), ('IM', 'Areas to Improve'), ('SU', 'Success'), ('FA', 'Failue'), ('O', 'Other')], default='GE', max_length=20),
        ),
    ]
