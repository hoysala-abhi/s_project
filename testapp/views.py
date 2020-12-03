from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import otp_data

def testapp(request):
  return HttpResponse('teeee')

def OTP(request):
   return HttpResponse('All the best')

def dbtest(request):
    if request.method == 'POST':
        email = request.POST['email']
        OTP = request.POST['OTP']

        otp_data1 = otp_data(email=email, OTP=OTP)
        otp_data1.save()
        return HttpResponse('all the best1')
    else:
        return HttpResponse('all the best')




