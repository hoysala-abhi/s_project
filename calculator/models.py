from django.db import models

# Create your models here.
class employees(models.Model):
    username = models.CharField(max_length=20,default='')
    name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    salary = models.IntegerField()
    Is_Permanent = models.BooleanField()
