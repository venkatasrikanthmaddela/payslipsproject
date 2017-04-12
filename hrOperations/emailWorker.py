import os

import pdfkit
from xhtml2pdf import pisa
import cStringIO as StringIO
from hrOperations.utils import get_html_string, get_payslip_date, is_network_available
from payslipsproject import settings
from payslipsproject.constants import BULK_IMPORT_ERROR_CODES, BULK_IMPORT_ERROR_SCHEMA
from payslipsproject.mailer import send_mail

__author__ = 'oliverqueen'

class EmailWorkerOps():
    def __init__(self, valid_data_objects, request):
        self.request = request
        self.filtered_user_data = valid_data_objects
        self.mail_status_list = dict(mailResultList = list(), errorResult=dict())

    def prepare_html_content(self):
        for each_record in self.filtered_user_data:
            html_string, pdf_string = get_html_string(each_record, self.request)
            each_record["htmlString"] = html_string
            each_record["pdfString"] = pdf_string
        return self.filtered_user_data

    def send_emails_to_the_users(self, user_content):
        for each_user_data in user_content:
            if each_user_data.get("email id") and is_network_available():
                result = StringIO.StringIO()
                # pdf = pisa.CreatePDF(StringIO.StringIO(each_user_data.get("pdfString").encode('utf-8')), result)
                # pdf = pisa.pisaDocument(StringIO.StringIO(each_user_data.get("pdfString").encode("UTF-8")), result, encoding="UTF-8")
                pdf = pdfkit.from_string(str(each_user_data.get("pdfString")), "")
                email_result = send_mail("Payslip for the month "+get_payslip_date(), each_user_data.get("htmlString"), each_user_data.get("email id"), pdf)
                self.mail_status_list["mailResultList"].append(email_result)
            else:
                self.mail_status_list["errorResult"] = {"errorCode":BULK_IMPORT_ERROR_SCHEMA.get("INTERNET CONNECTION"),
                                                        "errorMsg":BULK_IMPORT_ERROR_CODES.get(BULK_IMPORT_ERROR_SCHEMA.get("INTERNET CONNECTION"))}
                break
        return self.mail_status_list
