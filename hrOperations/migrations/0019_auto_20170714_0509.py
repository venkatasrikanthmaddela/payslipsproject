# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-14 05:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrOperations', '0018_auto_20170714_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payslipinfo',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 14, 5, 9, 49, 824062)),
        ),
        migrations.AlterField(
            model_name='payslipinfo',
            name='modifiedAt',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 14, 5, 9, 49, 824112)),
        ),
        migrations.AlterField(
            model_name='payslipuploads',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 14, 5, 9, 49, 824062)),
        ),
        migrations.AlterField(
            model_name='payslipuploads',
            name='modifiedAt',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 14, 5, 9, 49, 824112)),
        ),
        migrations.AlterField(
            model_name='smtpstatus',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 14, 5, 9, 49, 824062)),
        ),
        migrations.AlterField(
            model_name='smtpstatus',
            name='modifiedAt',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 14, 5, 9, 49, 824112)),
        ),
    ]
