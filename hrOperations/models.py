from datetime import datetime
from django.db import models
from payslipsproject.settings import DB_VERSION

__author__ = 'oliverqueen'

from payslipsproject.models import CustomModel

class PaySlipUploads(models.Model):
    dbVersion = models.CharField(max_length=20, default=DB_VERSION[-1])
    uploadedAt = models.DateTimeField()
    uploadedUser = models.CharField(max_length=256)
    noOfRecords = models.CharField(max_length=256)

class PaySlipInfo(models.Model):
    uploadId = models.ForeignKey(PaySlipUploads)
    uploadedDate = models.DateField(datetime.now().date().strftime('%d-%m-%Y'))
    employeeName = models.CharField(max_length=256)
    emailId = models.EmailField()
    department = models.CharField(max_length=256)
    designation = models.CharField(max_length=256)
    month = models.CharField(max_length=20)
    year = models.CharField(max_length=20)
    basic = models.FloatField()
    hra = models.FloatField()
    conveyance = models.FloatField()
    specialAllowance = models.FloatField()
    ot = models.FloatField()
    lta = models.FloatField()
    odr = models.FloatField()
    arrears = models.FloatField()
    educationAllowance = models.FloatField()
    medicalAllowance = models.FloatField()
    grossEarnings = models.FloatField()
    providentFund = models.FloatField()
    esi = models.FloatField()
    professionalTax = models.FloatField()
    incomeTax = models.FloatField()
    salaryAdvance = models.FloatField()
    cug = models.FloatField()
    lwf = models.FloatField()
    otherDeductions = models.FloatField()
    arrearsPFDeduction = models.FloatField()
    arrearsESIDeduction = models.FloatField()
    totalDeduction = models.FloatField()
    netPay = models.FloatField()
    emailStatus = models.BooleanField(default=False)

class smtpStatus(models.Model):
    date = models.DateField(default=datetime.now().date().strftime('%d-%m-%Y'))
    noOfMails = models.IntegerField()