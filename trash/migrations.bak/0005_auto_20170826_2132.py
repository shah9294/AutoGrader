# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-26 16:32
from __future__ import unicode_literals

import AutoGrade.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AutoGrade', '0004_auto_20170826_0234'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('enroll_key', models.CharField(max_length=12)),
                ('course_id', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_file', models.FileField(upload_to=AutoGrade.models.submission_directory_path)),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='as_code',
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='as_text',
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='section',
        ),
        migrations.RemoveField(
            model_name='section',
            name='rand_key',
        ),
        migrations.RemoveField(
            model_name='section',
            name='sec_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='section',
        ),
        migrations.AddField(
            model_name='assignment',
            name='assignment_file',
            field=models.FileField(default=None, upload_to=AutoGrade.models.assignment_directory_path),
        ),
        migrations.AddField(
            model_name='assignment',
            name='config_file',
            field=models.FileField(default=None, upload_to=AutoGrade.models.assignment_directory_path),
        ),
        migrations.AddField(
            model_name='assignment',
            name='description',
            field=models.TextField(default=None, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='assignment',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='due date'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='instructor_test',
            field=models.FileField(default=None, upload_to=AutoGrade.models.assignment_directory_path),
        ),
        migrations.AddField(
            model_name='assignment',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date published'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='student_test',
            field=models.FileField(default=None, upload_to=AutoGrade.models.assignment_directory_path),
        ),
        migrations.AddField(
            model_name='assignment',
            name='title',
            field=models.CharField(default=None, max_length=32),
        ),
        migrations.AddField(
            model_name='student',
            name='submission_pass',
            field=models.CharField(default=None, max_length=12),
        ),
        migrations.AddField(
            model_name='submission',
            name='assignment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AutoGrade.Assignment'),
        ),
        migrations.AddField(
            model_name='submission',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AutoGrade.Student'),
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ManyToManyField(to='AutoGrade.Instructor'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='course',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='AutoGrade.Course'),
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ManyToManyField(to='AutoGrade.Course'),
        ),
    ]