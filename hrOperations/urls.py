from hrOperations.views import BulkUploadUserPage, BulkPaySlipsPage, BulkPaySlipsFormat, PayslipsDashboardPage, \
  BulkExportPayslips

__author__ = 'oliverqueen'
from userManagement.api_views import loginUser, logoutUser, checkUserLogin

from django.conf.urls import url

urlpatterns = [
  url(r'users-upload-in-bulk', BulkUploadUserPage.as_view(), name="user-bulk-upload"),
  url(r'send-payslips-in-bulk', BulkPaySlipsPage.as_view(), name="user-payslips-upload"),
  url(r'download-bulk-payslips-template', BulkPaySlipsFormat.as_view(), name="export-sample-format"),
  url(r'bulk-export-pay-slips', BulkExportPayslips.as_view(), name="export-pay-slip-data"),
  url(r'payslips-dashboard', PayslipsDashboardPage.as_view(),name="payslips-dashboard-page")
]