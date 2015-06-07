# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aidatlar', '0002_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='balance',
            field=models.IntegerField(default=-30),
        ),
    ]
