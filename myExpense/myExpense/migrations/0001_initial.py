# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('catNum', models.AutoField(max_length=8, serialize=False, verbose_name=b'Category Num', primary_key=True)),
                ('catName', models.CharField(max_length=100, verbose_name=b'Category Name')),
                ('color', models.CharField(max_length=100, verbose_name=b'Color', choices=[(b'whiteButton', b'whiteButton'), (b'redButton', b'redButton'), (b'blueButton', b'blueButton'), (b'greenButton', b'greenButton'), (b'tealButton', b'tealButton'), (b'orangeButton', b'orangeButton')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['catName'],
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transID', models.AutoField(max_length=8, serialize=False, verbose_name=b'Transaction ID', primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'Title')),
                ('description', models.CharField(max_length=100, null=True, verbose_name=b'Description')),
                ('transType', models.CharField(max_length=100, verbose_name=b'Transaction Type', choices=[(b'+', b'+'), (b'-', b'-')])),
                ('amount', models.FloatField()),
                ('date', models.DateField(verbose_name=b'Transaction Date')),
                ('category', models.ForeignKey(to='myExpense.Category')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
