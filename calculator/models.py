from django.db import models

class signup_users(models.Model):
    username = models.CharField(max_length=20,default='')
    name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    password= models.CharField(max_length=20)

class otp_data(models.Model):
    email = models.EmailField()
    OTP = models.IntegerField()

