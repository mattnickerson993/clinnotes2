# Generated by Django 3.0.12 on 2021-02-23 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210223_1420'),
        ('reflections', '0003_auto_20210221_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reflection',
            name='episode_of_care',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reflections', to='users.EpisodeOfCare'),
        ),
    ]
