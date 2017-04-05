from hrOperations.utils import get_html_string
from payslipsproject.mailer import send_mail

__author__ = 'oliverqueen'

class EmailWorkerOps():
    def __init__(self, valid_data_objects, request):
        self.request = request
        self.filtered_user_data = valid_data_objects
        self.mail_status_list = list()

    def prepare_html_content(self):
        for each_record in self.filtered_user_data:
            html_string = get_html_string(each_record, self.request)
            each_record["htmlString"] = html_string
        return self.filtered_user_data

    def send_emails_to_the_users(self, user_content):
        for each_user_data in user_content:
            if each_user_data.get("email id"):
                email_result = send_mail("This Month Payslip", each_user_data.get("htmlString"), each_user_data.get("email id"))
                self.mail_status_list.append(email_result)
        return self.mail_status_list