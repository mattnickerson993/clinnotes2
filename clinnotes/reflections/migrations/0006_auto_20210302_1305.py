# Generated by Django 3.0.12 on 2021-03-02 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reflections', '0005_guidedreflection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reflection',
            name='category',
            field=models.CharField(choices=[('GE', 'General'), ('IM', 'Areas to Improve'), ('SU', 'Success'), ('FA', 'Failure'), ('O', 'Other')], default='GE', max_length=20),
        ),
    ]
