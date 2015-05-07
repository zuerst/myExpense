# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myExpense', '0013_auto_20150507_2301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='id',
        ),
        migrations.AddField(
            model_name='transaction',
            name='transID',
            field=models.AutoField(primary_key=True, default=1, serialize=False, max_length=8, verbose_name=b'Transaction ID'),
        ),
    ]
