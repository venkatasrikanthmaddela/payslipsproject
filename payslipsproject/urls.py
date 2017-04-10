"""payslipsproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import dashboardManagement
from payslipsproject.views import HomePage, SignInPage, EmailPage

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'api/user/', include('userManagement.api_urls')),
    url(r'hr-action', include('dashboardManagement.urls')),
    url(r'account/api/', include('userManagement.api_urls')),
    url(r'ops-hr/api/', include('hrOperations.api_urls')),
    url(r'ops-hr/', include('hrOperations.urls')),
    url(r'test-template', EmailPage.as_view()),
    url(r'', SignInPage.as_view(), name='home'),
]
