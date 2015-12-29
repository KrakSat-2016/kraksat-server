# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-29 21:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='GSInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(db_index=True, unique=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('timezone', models.IntegerField(help_text='Timezone as UTC offset in minutes (so e.g. UTC-01:45 becomes -105)')),
            ],
        ),
    ]