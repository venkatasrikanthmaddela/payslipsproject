import os

import pdfkit
# from xhtml2pdf import pisa
import cStringIO as StringIO
from hrOperations.utils import get_html_string, get_payslip_date, is_network_available, calculate_pay_slip, \
    get_html_string_from_db
from payslipsproject import settings
from payslipsproject.constants import BULK_IMPORT_ERROR_CODES, BULK_IMPORT_ERROR_SCHEMA, MONTHS
from payslipsproject.mailer import send_mail

__author__ = 'oliverqueen'

class EmailWorkerOps():
    def __init__(self, valid_data_objects, request):
        self.request = request
        self.filtered_user_data = valid_data_objects
        self.mail_status_list = dict(mailResultList = list(), errorResult=dict())
        self.model_data = object()

    def prepare_html_content(self):
        for each_record in self.filtered_user_data:
            html_string, pdf_string = get_html_string(each_record, self.request)
            each_record["htmlString"] = html_string
            each_record["pdfString"] = pdf_string
            each_record["otherCalculations"] = calculate_pay_slip(each_record)
        return self.filtered_user_data

    def prepare_html_data_from_db_data(self, db_model_data):
        self.model_data = db_model_data
        return get_html_string_from_db(db_model_data, self.request)


    def send_emails_to_the_users(self, user_content):
        try:
            if is_network_available():
                pdf = pdfkit.from_string(str(user_content.get("pdfString")), "")
                email_result = send_mail("Payslip for the month " + MONTHS.get(str(self.model_data.month)), user_content.get("htmlString"), self.model_data.emailId, pdf)
                self.mail_status_list["mailResultList"].append(email_result)
            else:
                 self.mail_status_list["errorResult"] = {"errorCode":BULK_IMPORT_ERROR_SCHEMA.get("INTERNET CONNECTION"),
                                                    "errorMsg":BULK_IMPORT_ERROR_CODES.get(BULK_IMPORT_ERROR_SCHEMA.get("INTERNET CONNECTION"))}
            return self.mail_status_list
        except Exception as e:
            self.mail_status_list["errorResult"] = {"errorCode": "500", "errorMsg": str(e.message)}
            return self.mail_status_list