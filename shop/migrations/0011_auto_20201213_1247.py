# Generated by Django 3.1.4 on 2020-12-13 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20201130_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='endtime',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='starttime',
            field=models.TimeField(null=True),
        ),
    ]
