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
    unit_1=models.TextField()
    unit_2=models.TextField()
    unit_3=models.TextField()
    unit_4=models.TextField()
    unit_5=models.TextField()
    def __str__(self):
        return u"%s" % self.name

class References(models.Model):
    name=models.CharField('Subject name',max_length=100)
    subjectid=models.IntegerField("Subject ID",unique=True,default=0)
    books=models.TextField(null=True)
    web=models.TextField('Web Sources',null=True)
    def __str__(self):
        return u"%s" % self.name

class Student(models.Model):
    user = models.OneToOneField(User,default=1,on_delete='CASCADE')
    username=models.CharField(max_length=50,default='')
    department = models.CharField("Department", max_length=4, choices=depts)
    year = models.IntegerField("Year", choices=[(i, i) for i in range(1, 5)])
    semester = models.IntegerField("Semester", choices=[(1, 1), (2, 2)])
    def __str__(self):
        return self.username