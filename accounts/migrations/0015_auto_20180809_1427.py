# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-09 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20180809_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='/static/img/blank_avatar.png', null=True, upload_to='img'),
        ),
    ]
