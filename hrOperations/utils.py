from collections import Counter
import re
from datetime import datetime
from django.core import serializers
from django.shortcuts import render_to_response
from django.template import RequestContext, Context
from django.template.loader import render_to_string, get_template
# import pdfkit
from hrOperations.models import PaySlipInfo, smtpStatus
from payslipsproject.constants import MANDATORY_FIELDS_FOR_PAYSLIP, BULK_IMPORT_ERROR_SCHEMA, BULK_IMPORT_ERROR_CODES, \
    PAYSLIPS_UPLOAD_FORMAT, PAYSLIPS_UPLOAD_FORMAT_VERSION, DEDUCTION_FIELDS, EARNING_FIELDS, COMPANY_DETAILS, \
    ACTUAL_EARNING_FIELDS
from payslipsproject.settings import STATIC_CDN_URL, SMTP_MAIL_LIMIT
import requests

__author__ = 'oliverqueen'

from xlrd import open_workbook

from validate_email import validate_email


class ExcelOperations():
    def __init__(self, input_file):
        self.input_file = input_file
        self.col_headers = list()
        self.work_sheet_data_list = list()
        self.validation_report = dict(result={})

    def extract_data_from_excel(self):
        work_book = open_workbook(file_contents=self.input_file.read())
        work_sheet = work_book.sheet_by_index(0)
        for col_index in xrange(work_sheet.ncols):
            col_header = work_sheet.cell(0, col_index).value
            self.col_headers.append(col_header.lower())
        for row_index in xrange(1, work_sheet.nrows):
            row_dict = {self.col_headers[col_index]:work_sheet.cell(row_index,col_index).value for col_index in xrange(work_sheet.ncols)}
            self.work_sheet_data_list.append(row_dict)
        return self.work_sheet_data_list

    def validate_excel_data(self, excel_data_as_json):
        if not self.validation_report["result"]:
            self.check_for_mandatory_fields(excel_data_as_json)
        if not self.validation_report["result"]:
            self.check_for_empty_data(excel_data_as_json)
        if not self.validation_report["result"]:
            self.check_email_validation(excel_data_as_json)
        if not self.validation_report["result"]:
            self.check_for_data_format(excel_data_as_json)
        if not self.validation_report["result"]:
            self.check_email_duplication(excel_data_as_json)
        return self.validation_report

    def check_email_validation(self, excel_data_as_json):
        invalid_emails = list()
        for each_record in excel_data_as_json:
            each_email_id = each_record.get("email id")
            is_valid = validate_email(each_email_id)
            if not is_valid:
                invalid_emails.append(each_email_id)
        if invalid_emails:
            self.validation_report["result"] = {"errorCode": BULK_IMPORT_ERROR_SCHEMA.get("INVALID EMAILS"),
                                                "errorMsg": BULK_IMPORT_ERROR_CODES.get(BULK_IMPORT_ERROR_SCHEMA.get("INVALID EMAILS")),
                                                "other": invalid_emails
                                                }
    def check_email_duplication(self, excel_data_as_json):
        all_email_ids = []
        duplicate_emails = []
        for each_record in excel_data_as_json:
            all_email_ids.append(each_record.get("email id"))
        duplicate_emails = [k for k, v in Counter(all_email_ids).items() if v > 1]
        if duplicate_emails:
            self.validation_report["result"] = {"errorCode": BULK_IMPORT_ERROR_SCHEMA.get("DUPLICATES"),
                                                "errorMsg": BULK_IMPORT_ERROR_CODES.get(BULK_IMPORT_ERROR_SCHEMA.get("DUPLICATES")),
                                                "other": duplicate_emails
                                                }

    def check_for_mandatory_fields(self, excel_data_as_json):
        keys_list = [each_key.lower() for each_key in excel_data_as_json[0].keys()]
        for mandatory_fields in MANDATORY_FIELDS_FOR_PAYSLIP:
            if mandatory_fields.lower() not in keys_list:
                self.validation_report["result"] = {"errorCode": BULK_IMPORT_ERROR_SCHEMA.get("HEADER MISMATCH"),
                                                    "errorMsg": BULK_IMPORT_ERROR_CODES.get(BULK_IMPORT_ERROR_SCHEMA.get("HEADER MISMATCH"))
                                                    }
    def check_for_empty_data(self, excel_data_as_json):
        for each_record in excel_data_as_json:
            for key, value in each_record.items():
                if key in MANDATORY_FIELDS_FOR_PAYSLIP and not value:
                    print key
                    self.validation_report["result"] = {"errorCode": BULK_IMPORT_ERROR_SCHEMA.get("DATA MISSING"),
                                                        "errorMsg": BULK_IMPORT_ERROR_CODES.get(BULK_IMPORT_ERROR_SCHEMA.get("DATA MISSING"))
                                                        }

    def check_for_data_format(self, excel_data_as_json):
        for each_record in excel_data_as_json:
            for key, value in each_record.items():
                if str(type(value)) not in PAYSLIPS_UPLOAD_FORMAT.get(PAYSLIPS_UPLOAD_FORMAT_VERSION[-1]).get(key.lower()):
                    self.validation_report["result"] = {"errorCode": BULK_IMPORT_ERROR_SCHEMA.get("DATA FORMAT ERROR"),
                                                        "errorMsg": BULK_IMPORT_ERROR_CODES.get(BULK_IMPORT_ERROR_SCHEMA.get("DATA FORMAT ERROR")),
                                                        "other": key
                                                        }
class PaySlipEmailOps():
    def __init__(self, extracted_json):
        self.extracted_excel_data = extracted_json
        self.analyzed_data = dict(alreadySentUsers=list())
        self.mail_count_report = dict(result=dict())

    def check_for_unique_entries(self):
        all_email_ids_of_excel_data = list()
        email_ids_of_previous_users = list()
        for each_record in self.extracted_excel_data:
            all_email_ids_of_excel_data.append(each_record.get("email id"))
        try:
            users_list_of_email_archives = PaySlipInfo.objects.filter(uploadedDate=datetime.now().date(), emailStatus=True)
            if users_list_of_email_archives:
                for each_user in users_list_of_email_archives:
                    email_ids_of_previous_users.append(each_user.emailId)
                for each_email in all_email_ids_of_excel_data:
                    if each_email in email_ids_of_previous_users:
                        self.analyzed_data["alreadySentUsers"].append(each_email)
        except:
            self.analyzed_data["alreadySentUsers"] = list()
        return self.analyzed_data

    def push_data_to_send_emails(self, analysis_data, extracted_data):
        filtered_data_to_push = list()
        for each_record in extracted_data:
            if each_record.get("email id") not in analysis_data.get("alreadySentUsers"):
                filtered_data_to_push.append(each_record)
        return filtered_data_to_push

    def check_for_mail_limit(self, mail_records):
        try:
            mail_status_register = smtpStatus.objects.get(date=datetime.now().date())
            no_of_mails_remaining = SMTP_MAIL_LIMIT - mail_status_register.noOfMails
            if len(mail_records) > no_of_mails_remaining or len(mail_records) > SMTP_MAIL_LIMIT:
                self.mail_count_report["result"] = {
                    "errorCode":BULK_IMPORT_ERROR_SCHEMA.get("MAILS LIMIT EXCEEDED"),
                    "errorMsg":BULK_IMPORT_ERROR_CODES.get(BULK_IMPORT_ERROR_SCHEMA.get("MAILS LIMIT EXCEEDED"))+"you can only send "+str(no_of_mails_remaining)+" mails for today"
                }
        except:
            print "Data doesn't exist in db"
        return self.mail_count_report


def get_html_string(data_dict, request):
    # html_safe_string = render_to_string('baseTemplates/emailTemplate.html', RequestContext(request, {"STATIC_CDN_URL":STATIC_CDN_URL, "companyDetails":COMPANY_DETAILS, "paySlipData":pay_slip_data, "request":request}))
    # pdf_string = render_to_string('baseTemplates/pdfTemplate.html', RequestContext(request, {"STATIC_CDN_URL":STATIC_CDN_URL, "companyDetails":COMPANY_DETAILS, "paySlipData":pay_slip_data, "request":request}))
    html_safe_string = ""
    pdf_string = ""
    return html_safe_string, pdf_string


def get_html_string_from_db(model_data, request):
    mail_body_data = {}
    mail_body_data["htmlString"] = render_to_string('baseTemplates/emailTemplate.html', RequestContext(request, {"STATIC_CDN_URL":STATIC_CDN_URL, "companyDetails":COMPANY_DETAILS, "paySlipData":model_data, "request":request}))
    mail_body_data["pdfString"] = render_to_string('baseTemplates/pdfTemplate.html', RequestContext(request, {"STATIC_CDN_URL":STATIC_CDN_URL, "companyDetails":COMPANY_DETAILS, "paySlipData":model_data, "request":request}))
    return mail_body_data



def calculate_pay_slip(data_dict):
    pay_slip_struct = dict(deductions=dict(), grossEarnings=dict(), totalDeductions="", totalEarnings="", totalNetPay="", basicDetails=dict(), actualGrossEarnings=dict())
    deductions_list = []
    earnings_list = []
    actual_earnings_list = []
    for key, value in data_dict.items():
        if key.lower() in DEDUCTION_FIELDS and value:
            pay_slip_struct["deductions"].update({key:value})
            deductions_list.append(value)
        elif key.lower() in EARNING_FIELDS:
            if value:
                pay_slip_struct["grossEarnings"].update({key : value})
                earnings_list.append(value)
        elif key.lower() in ACTUAL_EARNING_FIELDS:
            if value:
                pay_slip_struct["actualGrossEarnings"].update({key: value})
                actual_earnings_list.append(value)
        else:
            pay_slip_struct["basicDetails"].update({key: value})
    pay_slip_struct["totalDeductions"] = sum(deductions_list)
    pay_slip_struct["grossEarnings"] = sum(earnings_list)
    pay_slip_struct["actualGrossEarnings"] = sum(actual_earnings_list)
    pay_slip_struct["totalNetPay"] = sum(actual_earnings_list)-sum(deductions_list)
    return pay_slip_struct


def get_payslip_date():
    today_date = datetime.now().date().strftime('%B, %Y')
    return today_date

def is_network_available():
    try:
        requests.get("http://www.google.com")
        return True
    except requests.ConnectionError:
        return False
