# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-17 14:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('features', '0002_featurecomments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(default='example@example.com', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('feature', models.ForeignKey(default='Feature', on_delete=django.db.models.deletion.CASCADE, to='features.Feature')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.Order')),
            ],
        ),
    ]