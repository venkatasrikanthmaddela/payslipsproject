__author__ = 'oliverqueen'

from django.shortcuts import render
from django.views.generic import View

class HomePage(View):
    def get(self, request):
        return render(request, "baseTemplates/base.html")

class SignInPage(View):
    def get(self, request):
        return render(request, "baseTemplates/signInPage.html", {"request":request})
