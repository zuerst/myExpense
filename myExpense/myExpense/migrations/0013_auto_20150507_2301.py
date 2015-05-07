# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('myExpense', '0012_auto_20150507_2255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='id',
        ),
        migrations.AddField(
            model_name='category',
            name='catNum',
            field=models.AutoField(primary_key=True, default=1, serialize=False, max_length=8, verbose_name=b'Category Num'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.ForeignKey(default=1, to='myExpense.Category', null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
