# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2020-04-09 19:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
        ('courses', '0005_video_learn_times'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.Teacher', verbose_name='\u8bb2\u5e08'),
        ),
    ]
