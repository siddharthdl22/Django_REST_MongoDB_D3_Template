# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 00:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('grade', models.IntegerField()),
            ],
        ),
    ]