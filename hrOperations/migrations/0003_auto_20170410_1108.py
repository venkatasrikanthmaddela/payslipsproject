# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-10 11:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrOperations', '0002_auto_20170410_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='payslipinfo',
            name='bankAccountNumber',
            field=models.CharField(default=b'Not Provided', max_length=256),
        ),
        migrations.AddField(
            model_name='payslipinfo',
            name='bankName',
            field=models.CharField(default=b'IDBI', max_length=256),
        ),
        migrations.AddField(
            model_name='payslipinfo',
            name='effectiveWorkDays',
            field=models.FloatField(default=25),
        ),
        migrations.AddField(
            model_name='payslipinfo',
            name='employeeNumber',
            field=models.CharField(default=b'Not Provided', max_length=20),
        ),
        migrations.AddField(
            model_name='payslipinfo',
            name='location',
            field=models.CharField(default=b'KUKATPALLY', max_length=30),
        ),
        migrations.AddField(
            model_name='payslipinfo',
            name='panNumber',
            field=models.CharField(default=b'Not Provided', max_length=30),
        ),
        migrations.AddField(
            model_name='payslipinfo',
            name='ppfNumber',
            field=models.CharField(default=b'Not Provided', max_length=30),
        ),
        migrations.AlterField(
            model_name='payslipinfo',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 10, 11, 8, 52, 303257)),
        ),
        migrations.AlterField(
            model_name='payslipinfo',
            name='modifiedAt',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 10, 11, 8, 52, 303344)),
        ),
        migrations.AlterField(
            model_name='payslipuploads',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 10, 11, 8, 52, 303257)),
        ),
        migrations.AlterField(
            model_name='payslipuploads',
            name='modifiedAt',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 10, 11, 8, 52, 303344)),
        ),
        migrations.AlterField(
            model_name='smtpstatus',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 10, 11, 8, 52, 303257)),
        ),
        migrations.AlterField(
            model_name='smtpstatus',
            name='modifiedAt',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 10, 11, 8, 52, 303344)),
        ),
    ]
