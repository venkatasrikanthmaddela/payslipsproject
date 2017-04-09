__author__ = 'oliverqueen'

from django.shortcuts import render
from django.views.generic import View
from hrOperations.utils import calculate_pay_slip
from payslipsproject.constants import SAMPLE_DICT, COMPANY_DETAILS
from payslipsproject.settings import STATIC_CDN_URL
from django.template import RequestContext, Context

class HomePage(View):
    def get(self, request):
        return render(request, "baseTemplates/base.html")

class SignInPage(View):
    def get(self, request):
        return render(request, "baseTemplates/signInPage.html", {"request":request})


class EmailPage(View):
    def get(self, request):
        pay_slip_data = calculate_pay_slip(SAMPLE_DICT)
        return render(request, 'baseTemplates/emailTemplate.html', {"STATIC_CDN_URL":STATIC_CDN_URL,"companyDetails":COMPANY_DETAILS, "paySlipData":pay_slip_data, "request":request})