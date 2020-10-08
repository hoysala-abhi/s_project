from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail

from calculator.models import signup_users, otp_data
from s_project import settings
from django.conf import settings
from django.utils.crypto import get_random_string


def home(request):
  return render(request,'home.html')

def add(request) :
  val1 = int(request.POST["num1"])
  val2 = int(request.POST["num2"])
  Output= val1+val2
  return render(request, "Result.html", {'result':Output})

def multiply(request) :
  val1 = int(request.POST["num1"])
  val2 = int(request.POST["num2"])
  Mult_Output= val1*val2
  return render(request, "Result.html", {'result':Mult_Output})

def test_page(request):
  return HttpResponse('teeee')

def wish(request):
  return HttpResponse('Hi, Good Morning')

def signup(request):
  if request.method == 'POST':

    username=request.POST['username']
    name = request.POST['name']
    mobile = request.POST['mobile']
    email = request.POST['email']
    password = request.POST['password']
    x= signup_users(username = username, name= name,
                               mobile =mobile,
                               email= email,
                               password= password)
    x.save()
    otp = get_random_string(length=4, allowed_chars='1234567890')


    subject = 'Verify your Email'
    message = 'Hello  ' + x.name + '\n' + '\n' +' This is a verification Email' + '\n' + '\n' +'Your OTP is ' + otp
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [x.email]
    send_mail(subject, message, email_from, recipient_list)
    print("User_registered")
    return render(request, 'Email_confirmation.html')
  else :
    return render(request, 'Signup.html')

def email_confirmation(request):
  if request.method == 'POST':

    email = request.POST['email']
    OTP = request.POST['OTP']

    y= otp_data(email= email, OTP=OTP)
    y.save()
    print("User_registered")
    return HttpResponse("OTP Stored in DB along with EMail ")

  else:
    return render(request, 'email_confirmation.html')
