from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from calculator.models import signup_users, otp_data
from s_project import settings
from django.conf import settings
from django.utils.crypto import get_random_string
#from calculator.models import *
from django.db import models

def home(request):
    return render(request, 'home.html')

def add(request):
    val1 = int(request.POST["num1"])
    val2 = int(request.POST["num2"])
    Output = val1 + val2
    return render(request, "Result.html", {'result': Output})

def signup(request):
    otp_gen = get_random_string(length=4, allowed_chars='1234567890')
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        mobile = request.POST['mobile']
        email = request.POST['email']
        password = request.POST['password']
        otp_object = otp_gen

        x = signup_users(username=username, name=name, mobile=mobile,email=email, password=password,otp=otp_object)
        x.save()
        y = otp_data(email=email, OTP=otp_gen)
        y.save()

        # # email_part - working fine
        subject = 'Verify your Email'
        message = 'Hello  ' + x.name + ' This is a verification Email' + 'Your OTP is ' + otp_gen
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [x.email]
        send_mail(subject, message, email_from, recipient_list)

        print("User_registered")
        return render(request, 'Email_confirmation.html')
    else:
        return render(request, 'Signup.html')

def email_confirmation(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        cust_ent_otp = request.POST.get('OTP')

        queried_otp = signup_users.objects.filter(email=email).latest('email') # this will pick the whole row from DB where email = queried OTP
        #if y.OTP == queried_otp:
            #y.verified_user = True
        otp_gen=str(queried_otp.otp) # this will pick up the column from the queried_otp object. 0 th line is 1st line

        if otp_gen == None:
            # raise exception
            return HttpResponse("No email found")
        if otp_gen != cust_ent_otp:
            return HttpResponse("OTP didnt match ")
        if otp_gen == cust_ent_otp:
            a= signup_users.objects.filter(email=email)[0] # Filter() is used instead of get() because get gets only 1 
                                                            # Number should be equal to otp_gen.
            a.verified_user=True
            a.save()

        return HttpResponse("OTP Stored in DB along with EMail ")
    else:
        return render(request, 'email_confirmation.html')

    # Error : if verified user is already true and if you are entering OTP , its getting an error+test
    
def db_change_trial(request):
    a= signup_users.objects.get(name='aaa')
    a.name="bbb"
    a.save()
    return HttpResponse('TABLE ALTERED')

def testapp(request):
  return HttpResponse('teeee')