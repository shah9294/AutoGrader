# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-26 18:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AutoGrade', '0007_auto_20170826_2153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='course',
            new_name='courses',
        ),
    ]