# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-16 13:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20180716_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='feature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contribution', to='features.Feature'),
        ),
    ]
