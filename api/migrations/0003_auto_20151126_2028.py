# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_imu'),
    ]

    operations = [
        migrations.AddField(
            model_name='sht',
            name='id',
            field=models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sht',
            name='timestamp',
            field=models.DateTimeField(db_index=True, unique=True),
        ),
    ]
