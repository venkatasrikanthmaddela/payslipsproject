from hrOperations.api_views import PayslipGeneration, SendPaySlipsInBulk

__author__ = 'oliverqueen'
from django.conf.urls import url

urlpatterns = [
    url('payslips-in-bulk', PayslipGeneration.as_view()),
    url('send-payslips-emails-in-bulk', SendPaySlipsInBulk.as_view())
]