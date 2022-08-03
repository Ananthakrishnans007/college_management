
from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    Course_Name=models.CharField(max_length=255)
    Fee=models.IntegerField()

    def __str__(self):
        return self.Course_Name


class Student(models.Model):
    Course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    Student_Name=models.CharField(max_length=255)
    Address=models.CharField(max_length=255)
    Age=models.IntegerField()
    Join_date=models.DateField()
    Phone=models.CharField(max_length=12)

class Tutor(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Address=models.CharField(max_length=255)
    Gender=models.CharField(max_length=10)
    Course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    Phone=models.CharField(max_length=12)
    Image=models.ImageField(upload_to='image/tutor',default='image/tutor/default.png')

    def __str__(self):
        return self.user.username

        



