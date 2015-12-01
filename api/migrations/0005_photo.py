# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_gps'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(db_index=True, unique=True)),
                ('image', models.ImageField(upload_to='')),
                ('is_panorama', models.BooleanField()),
            ],
        ),
    ]
