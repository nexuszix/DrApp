# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbapi', '0003_auto_20170128_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drmas',
            name='clinic',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='drmas',
            name='prefix',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='drmas',
            name='specialty',
            field=models.CharField(max_length=100),
        ),
    ]