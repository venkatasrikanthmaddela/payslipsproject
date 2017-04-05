__author__ = 'oliverqueen'

from django.shortcuts import render
from django.views.generic import View
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout