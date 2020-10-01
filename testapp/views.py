from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import otp_data

def testapp(request):
  return HttpResponse('teeee')

def OTP(request):
   return HttpResponse('All the best')

