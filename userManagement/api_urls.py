from userManagement.api_views import loginUser, logoutUser, checkUserLogin

__author__ = 'oliverqueen'

from django.conf.urls import url

urlpatterns = [
   url('admin-login', loginUser.as_view(), name='login'),
   url('logout',logoutUser, name='log-out'),
   url('is-user-logged-in', checkUserLogin.as_view()),
]
