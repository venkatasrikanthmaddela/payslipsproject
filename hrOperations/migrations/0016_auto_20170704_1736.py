# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-04 17:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrOperations', '0015_auto_20170704_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payslipinfo',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 4, 17, 36, 4, 320538)),
        ),
        migrations.AlterField(
            model_name='payslipinfo',
            name='modifiedAt',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 4, 17, 36, 4, 320591)),
        ),
        migrations.AlterField(
            model_name='payslipuploads',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 4, 17, 36, 4, 320538)),
        ),
        migrations.AlterField(
            model_name='payslipuploads',
            name='modifiedAt',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 4, 17, 36, 4, 320591)),
        ),
        migrations.AlterField(
            model_name='smtpstatus',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 4, 17, 36, 4, 320538)),
        ),
        migrations.AlterField(
            model_name='smtpstatus',
            name='modifiedAt',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 4, 17, 36, 4, 320591)),
        ),
    ]
