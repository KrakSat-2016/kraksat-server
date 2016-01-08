# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-08 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='mission_time',
            field=models.FloatField(help_text='Current mission time in seconds. Negative value means countdown to start', null=True),
        ),
    ]