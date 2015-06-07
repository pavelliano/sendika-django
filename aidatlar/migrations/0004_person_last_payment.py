# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aidatlar', '0003_person_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='last_payment',
            field=models.DateTimeField(null=True),
        ),
    ]
