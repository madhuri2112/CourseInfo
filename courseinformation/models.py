from django.contrib.auth.models import User
from django.db import models

# Create your models here.
depts = [
    ('CSE', 'Computer Science'),
    ('ECE', 'Electronics and Communication'),
    ('IT', 'Information Technology')
]

class Subject(models.Model):
    name=models.CharField("Subject Name",max_length=100)
    subjectid=models.IntegerField("Subject ID",unique=True,default=0)
    department=models.CharField("Department",max_length=4,choices=depts)
    year=models.IntegerField("Year",choices=[(i,i) for i in range(1,5)])
    semester=models.IntegerField("Semester",choices=[(1,1),(2,2)])
    isopenelective=models.BooleanField("Open Elective",default=0)
    isprofessionalelective=models.BooleanField("Professional Elective",default=0)
    unit_1=models.TextField()
    unit_2=models.TextField()
    unit_3=models.TextField()
    unit_4=models.TextField()
    unit_5=models.TextField()
    def __str__(self):
        return self.name+"(id:"+str(self.subjectid)+")"

class References(models.Model):
    subject=models.OneToOneField(Subject,default=1,on_delete=models.CASCADE)
    subjectid=models.IntegerField("Subject ID",unique=True,default=0)
    books=models.TextField(null=True)
    web=models.TextField('Web Sources',null=True)
    def __str__(self):
        return str(self.subject)

class Student(models.Model):
    user = models.OneToOneField(User,default=1,on_delete=models.CASCADE)
    username=models.CharField(unique=True,max_length=50,default='')
    fullname=models.CharField(max_length=50,default='')
    joiningyear=models.IntegerField("Joining Year",choices=[(i,i) for i in range(2016,2030)],default=2022)
    department = models.CharField("Department", max_length=4, choices=depts)
    def __str__(self):
        return self.username+"("+self.fullname+")"

class Elective(models.Model):
    studentid = models.CharField(unique=True,max_length=50,default='-')
    oe1 = models.IntegerField(default=0)
    oe2 = models.IntegerField(default=0)
    oe3 = models.IntegerField(default=0)
    pe1 = models.IntegerField(default=0)
    pe2 = models.IntegerField(default=0)
    pe3 = models.IntegerField(default=0)
    def __str__(self):
        return self.studentid