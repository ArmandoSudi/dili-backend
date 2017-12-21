# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-21 11:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20171102_1632'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autopost',
            old_name='chassis',
            new_name='chassis_number',
        ),
        migrations.RenameField(
            model_name='autopost',
            old_name='doors',
            new_name='doors_number',
        ),
        migrations.RenameField(
            model_name='autopost',
            old_name='fuel',
            new_name='engine_type',
        ),
        migrations.RemoveField(
            model_name='autopost',
            name='color',
        ),
    ]
