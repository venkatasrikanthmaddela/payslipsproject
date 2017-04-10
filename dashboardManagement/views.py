from django.shortcuts import render
from django.views import View

__author__ = 'oliverqueen'


def DashboardPage(request):
    return render(request, "dashboardManagement/adminDashboard.html", {"request":request})