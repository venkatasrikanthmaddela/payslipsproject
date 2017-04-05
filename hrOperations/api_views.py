from hrOperations.emailWorker import EmailWorkerOps
from hrOperations.utils import ExcelOperations, PaySlipEmailOps, get_html_string
from payslipsproject.constants import BULK_IMPORT_ERROR_SCHEMA, BULK_IMPORT_ERROR_CODES

__author__ = 'oliverqueen'

from rest_framework.views import APIView
from rest_framework.response import Response

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
        filtered_data = pay_slip_ops_object.push_data_to_send_emails(result_info, extraced_data)
        email_prep_data_object = EmailWorkerOps(filtered_data, request)
        all_html_string = email_prep_data_object.prepare_html_content()
        email_status = email_prep_data_object.send_emails_to_the_users(all_html_string)
        print email_status
        return Response({"result": "success"}, 200)