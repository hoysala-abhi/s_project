from django.db import models

class otp_data(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    OTP = models.IntegerField()
    objects = models.Manager()

class extended(models.Model):
    username = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    objects = models.Manager()


