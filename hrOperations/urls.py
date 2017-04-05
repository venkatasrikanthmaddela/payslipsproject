from hrOperations.views import BulkUploadUserPage, BulkPaySlipsPage

__author__ = 'oliverqueen'
from userManagement.api_views import loginUser, logoutUser, checkUserLogin

from django.conf.urls import url

urlpatterns = [
  url(r'users-upload-in-bulk', BulkUploadUserPage.as_view(), name="user-bulk-upload"),
  url(r'send-payslips-in-bulk', BulkPaySlipsPage.as_view(), name="user-payslips-upload")
]