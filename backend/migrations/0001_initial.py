# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-10 16:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bundle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'bundle',
            },
        ),
        migrations.CreateModel(
            name='Button',
            fields=[
                ('button_id', models.CharField(max_length=64, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'button',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=128)),
                ('product_price', models.IntegerField()),
                ('product_stock', models.IntegerField()),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('button_id', models.CharField(max_length=64)),
                ('sequence_num', models.IntegerField()),
                ('record_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'record',
            },
        ),
        migrations.CreateModel(
            name='Regist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('button_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='button_regist', to='backend.Button')),
                ('cust_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'regist',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=128)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='record',
            name='regist_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Regist'),
        ),
        migrations.AddField(
            model_name='bundle',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Product'),
        ),
        migrations.AddField(
            model_name='bundle',
            name='regist_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Regist'),
        ),
        migrations.AlterUniqueTogether(
            name='regist',
            unique_together=set([('button_id', 'cust_id')]),
        ),
    ]