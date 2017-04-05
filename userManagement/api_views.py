from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from logger import logger
from payslipsproject.exceptions import UnAuthorizedException
from payslipsproject.utils import get_log_string

__author__ = 'oliverqueen'

from rest_framework.views import APIView


class loginUser(APIView):
    def post(self, request):
        USERMODEL = get_user_model()
        try:
            user = USERMODEL.objects.get(username=request.data.get("username"))
            user = authenticate(username=request.data.get("username"), password=request.data.get("password"), type='user')
            if user is None:
                raise UnAuthorizedException("Invalid User Name or Password")
            login(request, user)
            return Response({
                "result": user.username,
                "email": user.email,
                "name": user.username,
                "success": True
            }, 200)
        except USERMODEL.DoesNotExist:
            return Response({"error": "Invalid username or password"}, 500)
        except MultiValueDictKeyError as e:
            logger.error(get_log_string('error: '+str(e),request=request),exc_info=True)
            #This exception is raised when empty username or password is sent
            return Response({"error": "Invalid username or password"}, 500)
        except UnAuthorizedException as e:
            logger.error(get_log_string('error: '+str(e),request=request),exc_info=True)
            return Response({"error": e.message}, 401)
        except Exception as e:
            logger.error(get_log_string('error: '+str(e),request=request),exc_info=True)
            return Response({"error": str(e)}, 500)


@api_view(['GET','POST'])
def logoutUser(request):
    try:
        logout(request)
        return redirect('/')
    except Exception as e:
        logger.error(get_log_string('error: '+str(e),request=request),exc_info=True)
        return Response({}, 500)

class checkUserLogin(APIView):
    def get(self, request):
        try:
            email = request.user.email
            return Response({"success":email}, 200)
        except:
            return Response({"error": "user is not logged in"}, 500)