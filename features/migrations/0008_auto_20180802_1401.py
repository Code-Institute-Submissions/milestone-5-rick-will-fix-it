# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-02 14:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0007_auto_20180802_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='feature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='features.Feature'),
        ),
    ]
