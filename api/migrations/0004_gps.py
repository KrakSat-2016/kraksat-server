# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20151126_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='GPS',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('timestamp', models.DateTimeField(unique=True, db_index=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('altitude', models.FloatField(help_text='[m]')),
                ('direction', models.FloatField(help_text='Track Made Good (degrees relative to north) [°]')),
                ('speed_over_ground', models.FloatField(help_text='[km/h]')),
                ('active_satellites', models.PositiveSmallIntegerField()),
                ('satellites_in_view', models.PositiveSmallIntegerField()),
                ('quality', models.CharField(choices=[('no_fix', 'No Fix'), ('gps', 'GPS'), ('dgps', 'DGPS')], max_length=6)),
                ('fix_type', models.CharField(choices=[('no_fix', 'No fix'), ('2d', '2D'), ('3d', '3D')], max_length=6)),
                ('pdop', models.FloatField(verbose_name='PDOP', help_text='Position (3D) Dilution Of Precision')),
                ('hdop', models.FloatField(verbose_name='HDOP', help_text='Horizontal Dilution Of Precision')),
                ('vdop', models.FloatField(verbose_name='VDOP', help_text='Vertical Dilution Of Precision')),
            ],
        ),
    ]
