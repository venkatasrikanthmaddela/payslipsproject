__author__ = 'oliverqueen'
from django.shortcuts import render
from django.views.generic import View


class BulkUploadUserPage(View):
    def get(self, request):
        return render(request, "hrOperations/bulkUploadUser.html", {"request":request})


class BulkPaySlipsPage(View):
    def get(self, request):
        return render(request, "hrOperations/sendPayslipsInBulk.html", {"request":request})