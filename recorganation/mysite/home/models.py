from django.db import models
from django.contrib.sessions.models import Session
# Create your models here.

from django.utils import timezone

class Users(models.Model):
    uname=models.CharField(max_length=100)
    uemail=models.EmailField()
    upassword=models.CharField(max_length=15)

    class Meta:
        db_table = "users"
        # app_label = "users"


class Category(models.Model):
    c_id=models.CharField(max_length=100)
    c_name=models.CharField(max_length=100)

    class Meta:
        db_table = "category"


class Categoryvideo(models.Model):
    c_id=models.CharField(max_length=100)
    c_name=models.CharField(max_length=100)
    c_video_blob = models.BinaryField(default=bytes)
    c_video_file = models.FileField(upload_to='videos/')
    c_uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "categoryvideo"        



class Session(models.Model):
    user_id=models.CharField(max_length=50)
    sess_time=models.CharField(max_length=50)
    date= models.DateTimeField
    expires_at=  models.DateTimeField   

    class Meta:
        db_table = "session"   


def __str__(self):
        return self.name        