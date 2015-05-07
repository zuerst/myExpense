# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import myExpense.models


class Migration(migrations.Migration):

    dependencies = [
        ('myExpense', '0005_auto_20150506_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.ForeignKey(default=myExpense.models.Category, to='myExpense.Category'),
        ),
    ]
