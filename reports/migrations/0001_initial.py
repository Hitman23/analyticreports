# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-04 08:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=200)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('language', models.CharField(max_length=255, null=True)),
                ('urns', models.CharField(max_length=200)),
                ('groups', models.TextField()),
                ('fields', models.TextField(blank=True, null=True)),
                ('blocked', models.BooleanField(default=False)),
                ('stopped', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(null=True)),
                ('modified_on', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('expires', models.IntegerField()),
                ('active_runs', models.IntegerField(null=True)),
                ('complete_runs', models.IntegerField(null=True)),
                ('interrupted_runs', models.IntegerField(null=True)),
                ('expired_runs', models.IntegerField(null=True)),
                ('created_on', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('count', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_id', models.IntegerField()),
                ('broadcast', models.IntegerField(null=True)),
                ('urn', models.CharField(max_length=200)),
                ('channel', models.CharField(max_length=200)),
                ('direction', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('visibility', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=1000)),
                ('labels', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('sent_on', models.DateTimeField(blank=True, null=True)),
                ('modified_on', models.DateTimeField(blank=True, null=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lead', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('group', models.ManyToManyField(related_name='groups', to='reports.Group')),
            ],
        ),
        migrations.CreateModel(
            name='RapidproKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workspace', models.CharField(max_length=200)),
                ('host', models.CharField(max_length=200)),
                ('key', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run_id', models.IntegerField()),
                ('flow', models.CharField(max_length=200)),
                ('responded', models.BooleanField(default=False)),
                ('exit_type', models.CharField(blank=True, max_length=100, null=True)),
                ('exited_on', models.DateTimeField(null=True)),
                ('created_on', models.DateTimeField()),
                ('modified_on', models.DateTimeField()),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.Contact')),
            ],
        ),
    ]
