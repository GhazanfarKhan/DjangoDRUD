# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-19 21:44
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('joining_date', models.DateField(verbose_name='joining date')),
            ],
        ),
    ]
