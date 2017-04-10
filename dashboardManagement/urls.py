from dashboardManagement.views import DashboardPage

__author__ = 'oliverqueen'
from django.conf.urls import url
from django.contrib import admin
from payslipsproject.views import HomePage, SignInPage

urlpatterns = [
    url(r'/dashboard', DashboardPage, name="dashboard-page"),
]