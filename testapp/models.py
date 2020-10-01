from django.db import models

# Create your models here.
class otp_data(models.Model):
    email = models.EmailField()
    OTP = models.IntegerField()

