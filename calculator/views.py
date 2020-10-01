from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
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
    first_name= request.POST['name1']
    name2 = request.POST['name2']
    Email_ID = request.POST['e_mail']
    pw = request.POST['pw']
    x=User.objects.create_user(username = username, first_name= first_name,
                               last_name =name2,
                               email= Email_ID,
                               password= pw)
    x.save()

    otp = get_random_string(length=4, allowed_chars='1234567890')


    subject = 'Verify your Email'
    message = 'Hello  ' + x.first_name + '\n' + '\n' +' This is a verification Email' + '\n' + '\n' +'Your OTP is ' + otp
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [x.email]
    send_mail(subject, message, email_from, recipient_list)
    print("user_created")
    return render(request, 'Email_confirmation.html')

  else :
    return render(request, 'Signup.html')

def email_confirmation(request):
  return HttpResponse('email test')





