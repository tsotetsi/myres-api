# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-04 09:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myres', '0003_auto_20170404_0924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='residence',
        ),
    ]
