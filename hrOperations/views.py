import json

import operator

from datetime import datetime
from django.http import HttpResponse
from django.forms.models import model_to_dict
from hrOperations.models import PaySlipUploads, PaySlipInfo, smtpStatus
from payslipsproject.constants import PAYSLIPS_UPLOAD_FORMAT_VERSION, PAYSLIPS_UPLOAD_FORMAT, \
    PAYSLIPS_UPLOAD_TUPLE_FORMAT, SAMPLE_DATA

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
        try:
            no_of_mails =smtpStatus.objects.get(date=datetime.now().date()).noOfMails
        except:
            no_of_mails = 0
        return render(request, "hrOperations/sendPayslipsInBulk.html", {"request":request, "noOfMails":no_of_mails})


class PayslipsDashboardPage(View):
    def get(self,request):
        complete_payslips_data = get_all_payslips_data()
        return render(request, "hrOperations/paySlipsDashboard.html", {"request": request, "completePaySlipsData":complete_payslips_data})


class BulkPaySlipsFormat(View):
    def get(self, request):
        # data = PAYSLIPS_UPLOAD_FORMAT[PAYSLIPS_UPLOAD_FORMAT_VERSION[-1]]
        data = PAYSLIPS_UPLOAD_TUPLE_FORMAT[PAYSLIPS_UPLOAD_FORMAT_VERSION[-1]]
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('sampleDataSheet')
        data = OrderedDict((value, True) for value in data)
        sample_entry = OrderedDict((value, True) for value in SAMPLE_DATA)
        print data
        print sample_entry
        for index, value in enumerate(data):
            sheet.write(0, index, value)
        for index, value in enumerate(sample_entry):
            sheet.write(1, index, value)
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=payslip-upload-template.xls'
        workbook.save(response)
        return response

class BulkExportPayslips(View):
    def get(self, request):
        bulk_data = list()
        work_book = xlwt.Workbook()
        formatted_string = dict()
        work_sheet = work_book.add_sheet('paySlipsData')
        complete_obj_data = get_all_payslips_data()
        for key,value in complete_obj_data.items():
            for each_upload in value:
                each_upload = model_to_dict(each_upload)
                formatted_string.update({col_key:user_data}for col_key, user_data in each_upload.items())
                bulk_data.append(each_upload)
        print bulk_data
        columns = bulk_data[0].keys()
        for i, row in enumerate(bulk_data):
            for j, col in enumerate(columns):
                work_sheet.write(i, j, row[col])
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=payslips-bulk-data.xls'
        work_book.save(response)
        return response


def get_all_payslips_data():
    all_payslips_uploads = dict()
    all_uploads = PaySlipUploads.objects.all().order_by('uploadedAt')
    all_payslip_entries = PaySlipInfo.objects.all()
    if all_uploads:
        for each_upload_info in all_uploads:
            all_payslips_uploads[each_upload_info.uploadedAt] = list()
        for each_payslip_entry in all_payslip_entries:
            if each_payslip_entry.createdAt in all_payslips_uploads.keys():
                all_payslips_uploads[each_payslip_entry.createdAt].append(each_payslip_entry)
        all_payslips_uploads = OrderedDict(sorted(all_payslips_uploads.items(), reverse=True))
    return all_payslips_uploads
