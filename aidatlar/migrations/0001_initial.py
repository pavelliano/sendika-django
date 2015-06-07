# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('full_name', models.CharField(max_length=70)),
                ('subscription_date', models.DateTimeField(verbose_name=b'Uyelik Tarihi')),
                ('member_num', models.IntegerField(serialize=False, primary_key=True)),
                ('init_payment', models.ForeignKey(to='aidatlar.PaymentType')),
            ],
        ),
    ]
