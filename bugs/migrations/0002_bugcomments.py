# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-16 15:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bugs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BugComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('bug', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bugs.Bug')),
                ('user', models.ForeignKey(null=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
