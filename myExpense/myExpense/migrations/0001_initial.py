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
                ('catNum', models.AutoField(primary_key=True, default=1, serialize=False, max_length=8, verbose_name=b'Category Num')),
                ('mainCategory', models.CharField(max_length=100, verbose_name=b'Main Category')),
                ('subCategory', models.CharField(max_length=100, verbose_name=b'Sub Category')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transID', models.AutoField(primary_key=True, default=1, serialize=False, max_length=8, verbose_name=b'Transaction ID')),
                ('title', models.CharField(max_length=100, verbose_name=b'Title')),
                ('description', models.CharField(max_length=100, null=True, verbose_name=b'Description')),
                ('transType', models.CharField(max_length=100, verbose_name=b'Transaction Type', choices=[(b'Debit', b'Debit'), (b'Credit', b'Credit')])),
                ('amount', models.FloatField()),
                ('date', models.DateField(verbose_name=b'Transaction Date')),
                ('category_id', models.ForeignKey(default=1, to='myExpense.Category')),
                ('user_id', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
