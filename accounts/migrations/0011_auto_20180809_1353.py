# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-09 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20180809_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='{{ MEDIA_URL }}/img/blank_avatar.png', upload_to='img'),
        ),
    ]