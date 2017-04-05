__author__ = 'oliverqueen'

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from payslipsproject.settings import EMAIL_ID, EMAIL_ID_PASSWORD, SMTP_SERVER, SMTP_PORT


def send_mail(subject, body, receiver_list):
    mail_status = dict(result="")
    mail_user = EMAIL_ID
    mail_pwd = EMAIL_ID_PASSWORD
    from_id = mail_user
    to_ids = receiver_list  #must be a lista
    message = MIMEMultipart('alternative')
    message['Subject'] = subject
    message['From'] = 'CustomFurnish <'+from_id+'>'
    message['To'] = to_ids[0]
    part2 = MIMEText(body, 'html')
    message.attach(part2)
    smtp_server = SMTP_SERVER
    smtp_port = SMTP_PORT
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)  #or port 465 doesn't seem to work!
        server.ehlo()
        server.starttls()
        server.login(mail_user, mail_pwd)
        server.sendmail(from_id, to_ids, message.as_string())
        server.quit()
        mail_status["result"] = "Success fully mail sent"
        return mail_status
    except Exception as e:
        mail_status["result"] = "Failed sending mail to {0} Exception {1}".format(receiver_list,str(e))
        return mail_status
