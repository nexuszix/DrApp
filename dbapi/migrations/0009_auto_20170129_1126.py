# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 04:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbapi', '0008_auto_20170129_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drmas',
            name='drCode',
            field=models.CharField(blank=True, default=b'', max_length=20),
        ),
    ]