from django.db import models

# Create your models here.

class Teacher(models.Model):
    #id = models.Field(primary_key = True)
    mail = models.EmailField(default='teacher@teacher.com',unique=True)
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    def __str__(self): 
         return self.fName+" "+self.lName

class Student(models.Model):
    #id = models.Field(primary_key = True)
    mail = models.EmailField(default='student@student.com',unique=True)
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    year = models.PositiveIntegerField(default=1947)
    branch = models.CharField(max_length=50)
    rollNo = models.PositiveIntegerField(default=0,unique=True)
    DMgrade = models.CharField(max_length=2, default="NA")
    DCgrade = models.CharField(max_length=2, default="NA")
    COAgrade = models.CharField(max_length=2, default="NA")
    SEgrade = models.CharField(max_length=2, default="NA")
    PaSgrade = models.CharField(max_length=2, default="NA")
    DSgrade = models.CharField(max_length=2, default="NA")
    def __str__(self): 
         return self.fName+" "+self.lName