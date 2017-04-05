# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-05 11:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myres', '0004_remove_flat_residence'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='residence',
        ),
        migrations.AddField(
            model_name='application',
            name='residence',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myres.Residence'),
        ),
    ]
