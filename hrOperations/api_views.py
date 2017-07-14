from hrOperations.db_ops import UpdateInDb
from hrOperations.emailWorker import EmailWorkerOps
from hrOperations.utils import ExcelOperations, PaySlipEmailOps, get_html_string
from payslipsproject.constants import BULK_IMPORT_ERROR_SCHEMA, BULK_IMPORT_ERROR_CODES

__author__ = 'oliverqueen'

from rest_framework.views import APIView
from rest_framework.response import Response
import pdfkit


class PayslipGeneration(APIView):
    def post(self, request):
        input_excel = request.FILES['paySlipsFile']
        extracted_data = ExcelOperations(input_excel).extract_data_from_excel()
        if not extracted_data:
            return Response({"result":"error", "errorData": {"errorCode": BULK_IMPORT_ERROR_SCHEMA.get("SHEET EMPTY"),
                                                             "errorMsg": BULK_IMPORT_ERROR_CODES.get(BULK_IMPORT_ERROR_SCHEMA.get("SHEET EMPTY"))
                                                             }
                             },500)
        else:
            validation_report = ExcelOperations(input_excel).validate_excel_data(extracted_data)
            if validation_report["result"]:
                return Response({"result":"error", "errorData":validation_report["result"]}, 500)
            else:
                return Response({"result":"success", "jsonData": extracted_data}, 200)


class SendPaySlipsInBulk(APIView):
    def post(self, request):
        extraced_data = request.data
        pay_slip_ops_object = PaySlipEmailOps(extraced_data)
        result_info = pay_slip_ops_object.check_for_unique_entries()
        if len(result_info.get("alreadySentUsers")) == len(extraced_data):
            return Response({"result": "error", "errorData": {"errorCode": "emails already sent to ", "errorMsg": result_info.get("alreadySentUsers")}}, 500)
        filtered_data = pay_slip_ops_object.push_data_to_send_emails(result_info, extraced_data)
        mail_limit_report = pay_slip_ops_object.check_for_mail_limit(filtered_data)
        if mail_limit_report.get("result"):
            return Response({"result": "error", "errorData": mail_limit_report.get("result")}, 500)
        else:
            email_prep_data_object = EmailWorkerOps(filtered_data, request)
            all_html_string = email_prep_data_object.prepare_html_content()
            return Response({"result": "success", "userData":all_html_string, "alreadySent":result_info["alreadySentUsers"]}, 200)


class ProcessEmails(APIView):
    def post(self, request):
        try:
            initialize_db = UpdateInDb(request.data, request)
            uploaded_data = initialize_db.initiate_data_to_upload()
            for each_uploaded_data in uploaded_data:
                email_worker_ops = EmailWorkerOps([], request)
                email_body_data = email_worker_ops.prepare_html_data_from_db_data(each_uploaded_data)
                email_status = email_worker_ops.send_emails_to_the_users(email_body_data)
                if email_status.get("errorResult"):
                    return Response({"result": "error", "errorData": email_status.get("errorResult")}, 500)
                else:
                    each_uploaded_data.emailStatus = True
                    initialize_db.update_smtp_status()
            return Response({"result": "success"}, 200)
        except Exception as e:
            print "Sending mails failed due to.." + str(e.message)
            return Response({"result": "error"}, 500)
