from django.contrib import admin
from hrOperations.models import PaySlipUploads,PaySlipInfo,smtpStatus

admin.site.register(PaySlipUploads)
admin.site.register(PaySlipInfo)
admin.site.register(smtpStatus)
