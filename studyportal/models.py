from django.db import models

# Create your models here.
class Register(models.Model):
    username=models.CharField(null=False, max_length=50)
    mobile_no=models.IntegerField(null=False)
    email=models.CharField(max_length=15)
    password=models.CharField(max_length=255)

# class Contact(models.Model):
#     name=models.CharField(null=False, max_length=50)
#     email=models.CharField(max_length=50)
#     message=models.CharField(max_length=100)
    
