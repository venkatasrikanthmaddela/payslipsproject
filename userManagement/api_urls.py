from userManagement.api_views import loginUser, logoutUser, checkUserLogin, SignUpUser

__author__ = 'oliverqueen'

from django.conf.urls import url

urlpatterns = [
   url('admin-login', loginUser.as_view(), name='login'),
   # url('sign-up', SignUpUser.as_view()),
   url('logout',logoutUser, name='log-out'),
   url('is-user-logged-in', checkUserLogin.as_view()),
]
