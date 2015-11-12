# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SHT',
            fields=[
                ('timestamp', models.DateTimeField(primary_key=True, serialize=False)),
                ('humidity', models.DecimalField(max_digits=5, help_text='0 to 100%, resolution 0.04%', decimal_places=2)),
                ('temperature', models.DecimalField(max_digits=5, help_text='-40 to 125℃, resolution 0.01℃', decimal_places=2)),
            ],
        ),
    ]
