# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutoGrade', '0010_auto_20170831_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]