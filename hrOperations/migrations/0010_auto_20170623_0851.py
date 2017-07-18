# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-23 08:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrOperations', '0009_auto_20170410_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payslipinfo',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 23, 8, 51, 3, 235181)),
        ),
        migrations.AlterField(
            model_name='payslipinfo',
            name='modifiedAt',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 23, 8, 51, 3, 235232)),
        ),
        migrations.AlterField(
            model_name='payslipinfo',
            name='uploadedDate',
            field=models.DateField(verbose_name=datetime.date(2017, 6, 23)),
        ),
        migrations.AlterField(
            model_name='payslipuploads',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 23, 8, 51, 3, 235181)),
        ),
        migrations.AlterField(
            model_name='payslipuploads',
            name='modifiedAt',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 23, 8, 51, 3, 235232)),
        ),
        migrations.AlterField(
            model_name='smtpstatus',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 23, 8, 51, 3, 235181)),
        ),
        migrations.AlterField(
            model_name='smtpstatus',
            name='date',
            field=models.DateField(default=datetime.date(2017, 6, 23)),
        ),
        migrations.AlterField(
            model_name='smtpstatus',
            name='modifiedAt',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 23, 8, 51, 3, 235232)),
        ),
    ]
