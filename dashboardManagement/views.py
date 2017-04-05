from django.shortcuts import render
from django.views import View

__author__ = 'oliverqueen'


class DashboardPage(View):
    def get(self, request):
        return render(request, "dashboardManagement/adminDashboard.html", {"request":request})