from django.http import HttpResponse

from payslipsproject.constants import PAYSLIPS_UPLOAD_FORMAT_VERSION, PAYSLIPS_UPLOAD_FORMAT, \
    PAYSLIPS_UPLOAD_TUPLE_FORMAT

__author__ = 'oliverqueen'
import xlwt
from django.shortcuts import render
from django.views.generic import View
from collections import OrderedDict


class BulkUploadUserPage(View):
    def get(self, request):
        return render(request, "hrOperations/bulkUploadUser.html", {"request":request})


class BulkPaySlipsPage(View):
    def get(self, request):
        return render(request, "hrOperations/sendPayslipsInBulk.html", {"request":request})


class BulkPaySlipsFormat(View):
    def get(self, request):
        # data = PAYSLIPS_UPLOAD_FORMAT[PAYSLIPS_UPLOAD_FORMAT_VERSION[-1]]
        data = PAYSLIPS_UPLOAD_TUPLE_FORMAT[PAYSLIPS_UPLOAD_FORMAT_VERSION[-1]]
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('test')
        data = OrderedDict((value, True) for value in data)
        for index, value in enumerate(data):
            sheet.write(0, index, value)
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=payslip-upload-template.xls'
        workbook.save(response)
        return response