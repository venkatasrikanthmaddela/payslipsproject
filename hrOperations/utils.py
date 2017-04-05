from collections import Counter
import re
from datetime import datetime
from django.shortcuts import render_to_response
from django.template import RequestContext, Context
from django.template.loader import render_to_string, get_template
import pdfkit
from hrOperations.models import PaySlipInfo
from payslipsproject.constants import MANDATORY_FIELDS_FOR_PAYSLIP, BULK_IMPORT_ERROR_SCHEMA, BULK_IMPORT_ERROR_CODES, \
    PAYSLIPS_UPLOAD_FORMAT, PAYSLIPS_UPLOAD_FORMAT_VERSION
from payslipsproject.settings import STATIC_CDN_URL

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
                    self.validation_report["result"] = {"errorCode": BULK_IMPORT_ERROR_SCHEMA.get("DATA MISSING"),
                                                        "errorMsg": BULK_IMPORT_ERROR_CODES.get(BULK_IMPORT_ERROR_SCHEMA.get("DATA MISSING"))
                                                        }

    def check_for_data_format(self, excel_data_as_json):
        for each_record in excel_data_as_json:
            for key, value in each_record.items():
                if str(type(value)) not in PAYSLIPS_UPLOAD_FORMAT.get(PAYSLIPS_UPLOAD_FORMAT_VERSION[-1]).get(key.lower()):
                    self.validation_report["result"] = {"errorCode": BULK_IMPORT_ERROR_SCHEMA.get("DATA FORMAT ERROR"),
                                                        "errorMsg": BULK_IMPORT_ERROR_CODES.get(BULK_IMPORT_ERROR_SCHEMA.get("DATA FORMAT ERROR"))
                                                        }
class PaySlipEmailOps():
    def __init__(self, extracted_json):
        self.extracted_excel_data = extracted_json
        self.analyzed_data = dict(alreadySentUsers=list())

    def check_for_unique_entries(self):
        all_email_ids_of_excel_data = list()
        email_ids_of_previous_users = list()
        for each_record in self.extracted_excel_data:
            all_email_ids_of_excel_data.append(each_record.get("email id"))
        users_list_of_email_archives = PaySlipInfo.objects.filter(uploadedDate=datetime.now().date())
        if users_list_of_email_archives:
            for each_user in users_list_of_email_archives:
                email_ids_of_previous_users.append(each_user.emailId)
            for each_email in all_email_ids_of_excel_data:
                if each_email in email_ids_of_previous_users:
                    self.analyzed_data["alreadySentUsers"].append(each_email)
        else:
            self.analyzed_data["alreadySentUsers"] = list()
        return self.analyzed_data

    def push_data_to_send_emails(self, analysis_data, extracted_data):
        filtered_data_to_push = list()
        for each_record in extracted_data:
            if each_record.get("email id") not in analysis_data.get("alreadySentUsers"):
                filtered_data_to_push.append(each_record)
        return filtered_data_to_push


def get_html_string(data_dict, request):
    # template = get_template("baseTemplates/emailTemplate.html")
    # context = Context(request)
    # html_safe_string = template.render(context)
    html_safe_string = render_to_string('baseTemplates/emailTemplate.html', RequestContext(request, {"STATIC_CDN_URL":STATIC_CDN_URL, "request":request}))
    # pdfkit.from_string(html_safe_string, 'output.pdf')
    return html_safe_string
