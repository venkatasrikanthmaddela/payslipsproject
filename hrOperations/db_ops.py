from datetime import datetime

from hrOperations.models import smtpStatus, PaySlipInfo, PaySlipUploads
from payslipsproject.mailer import send_mail
from payslipsproject.settings import JOB_FAILURE_REPORT_GROUP


class UpdateInDb():
    def __init__(self, user_data, request):
        self.user_data = user_data
        self.request = request

    def initiate_data_to_upload(self):
        if self.user_data:
            pay_slip_data_object = PaySlipUploads(uploadedAt=datetime.now(), uploadedUser=self.request.user.email, noOfRecords=len(self.user_data))
            pay_slip_data_object.save()
            return self.save_db_entries(pay_slip_data_object)

    def update_smtp_status(self):
        try:
            mail_status_register = smtpStatus.objects.get(date=datetime.now().date())
            mail_status_register.noOfMails +=1
            mail_status_register.save()
        except smtpStatus.DoesNotExist:
            smtp_data_object = smtpStatus(date=datetime.now(), noOfMails=1)
            smtp_data_object.save()

    def save_db_entries(self, pay_slip_data_object):
        all_data_objects = []
        for each_record in self.user_data:
            try:
                payslip_info_object = PaySlipInfo(uploadId=pay_slip_data_object,
                                                  uploadedDate=datetime.now().date(),
                                                  employeeName=each_record.get("employee name"),
                                                  emailId=each_record.get("email id"),
                                                  department=each_record.get("department"),
                                                  designation=each_record.get("designation"),
                                                  month=each_record.get("month"),
                                                  year=each_record.get("year"),
                                                  basic=each_record.get("basic and da"),
                                                  hra=each_record.get("house rent allowance"),
                                                  conveyance=each_record.get("conveyance"),
                                                  specialAllowance=each_record.get("special allowance"),
                                                  ot=each_record.get("o.t"), lta=each_record.get("leave travel allowance"),
                                                  odr=each_record.get("other deduction reimbt"),
                                                  increment=each_record.get("increment"),
                                                  educationAllowance=each_record.get("edu allow"),
                                                  medicalAllowance=each_record.get("med. allowance"),
                                                  providentFund=each_record.get("provident fund"),
                                                  esi=each_record.get("esi"),
                                                  professionalTax=each_record.get("prof tax"),
                                                  incomeTax=each_record.get("income tax"),
                                                  salaryAdvance=each_record.get("salary advance"),
                                                  cug=each_record.get("cug"),
                                                  lwf=each_record.get("lwf"),
                                                  otherDeductions=each_record.get("other deductions"),
                                                  arrearsPFDeduction=each_record.get("arrears pf deduction"),
                                                  arrearsESIDeduction=each_record.get("arrears esi deduction"),
                                                  employeeNumber=each_record.get("employee number"),
                                                  bankName=each_record.get("bank name"),
                                                  bankAccountNumber=each_record.get("bank account number"),
                                                  panNumber=each_record.get("pan number"),
                                                  ppfNumber=each_record.get("ppf number"),
                                                  location=each_record.get("location"),
                                                  effectiveWorkDays=each_record.get("effective work days"),
                                                  emailStatus=False,
                                                  earnedBasicAndDa=each_record.get("earned basic and da"),
                                                  earnedHouseRentAllowance=each_record.get("earned house rent allowance"),
                                                  earnedConveyance=each_record.get("earned conveyance"),
                                                  earnedSpecialAllowance=each_record.get("earned special allowance"),
                                                  earnedOt=each_record.get("earned o.t"),
                                                  earnedLeaveTravelAllowance=each_record.get("earned leave travel allowance"),
                                                  earnedOtherDeductionReimbt=each_record.get("earned other deduction reimbt"),
                                                  earnedIncrement=each_record.get("earned increment"),
                                                  earnedEduAllow=each_record.get("earned edu allow"),
                                                  earnedMedAllowance=each_record.get("earned med. allowance"),
                                                  houseMaintenance=each_record.get("house maintenance"),
                                                  earnedHouseMaintenance=each_record.get("earned house maintenance"),
                                                  driverSalary = each_record.get("driver salary"),
                                                  earnedDriverSalary=each_record.get("earned driver salary"),
                                                  carMaintenance = each_record.get("car maintenance"),
                                                  earnedCarMaintenance = each_record.get("earned car maintenance"),
                                                  fuelReimbursement = each_record.get("fuel reimbursement"),
                                                  earnedFuelReimbursement = each_record.get("earned fuel reimbursement"),
                                                  incentives = each_record.get("incentives"),
                                                  earnedIncentives= each_record.get("earned incentives"),
                                                  grossEarnings=each_record.get("otherCalculations").get("grossEarnings"),
                                                  actualGrossEarnings= each_record.get("otherCalculations").get("actualGrossEarnings"),
                                                  totalDeduction=each_record.get("otherCalculations").get("totalDeductions"),
                                                  totalNetPay=each_record.get("otherCalculations").get("totalNetPay")
                                                  )
                payslip_info_object.save()
                all_data_objects.append(payslip_info_object)
            except Exception as e:
                mail_status = send_mail("data saving failed in db", str(each_record), JOB_FAILURE_REPORT_GROUP, "")
                if mail_status.get("result") == "Success fully mail sent":
                    mail_status_register = smtpStatus.objects.get(date=datetime.now().date())
                    mail_status_register.noOfMails +=1
                    mail_status_register.save()
        return all_data_objects

