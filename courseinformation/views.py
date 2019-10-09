import datetime

from django.shortcuts import render,redirect
from .models import Student,Subject,References,Elective
# Create your views here.

now = datetime.datetime.now()
getsemester = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2]

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'home.html',{})

def syllabus(request):
    student=Student.objects.filter(username=request.user.username)[0]
    studentyear,studentsem = (now.year - student.joiningyear) , getsemester[int(now.strftime("%m"))-1]
    subjects=Subject.objects.filter(department=student.department,year=studentyear,semester=studentsem)
    return render(request,'syllabus.html',{'subjects':subjects})

def reference(request):
    student=Student.objects.filter(username=request.user.username)[0]
    studentyear,studentsem = (now.year - student.joiningyear) , getsemester[int(now.strftime("%m"))-1]
    subjects=Subject.objects.filter(department=student.department,year=studentyear,semester=studentsem)
    return render(request,'reference.html',{'subjects':subjects})

def syllabusdetail(request,id):
    student=Student.objects.filter(username=request.user.username)[0]
    studentyear,studentsem = (now.year - student.joiningyear) , getsemester[int(now.strftime("%m"))-1]
    subjects=Subject.objects.filter(department=student.department,year=studentyear,semester=studentsem)
    subject=Subject.objects.filter(subjectid=id)[0]
    return render(request,'syllabusdetail.html',{'subjects':subjects,'subject':subject})

def referencedetails(request,id):
    student=Student.objects.filter(username=request.user.username)[0]
    studentyear,studentsem = (now.year - student.joiningyear) , getsemester[int(now.strftime("%m"))-1]
    subjects=Subject.objects.filter(department=student.department,year=studentyear,semester=studentsem)
    reference=References.objects.filter(subjectid=id)[0]
    return render(request,'referencedetails.html',{'subjects':subjects,'reference':reference})

def myelective(request):
    openelectives=Subject.objects.filter(isopenelective=True)
    professionalelectives = Subject.objects.filter(isprofessionalelective=True)
    return render(request,'myelective.html',{'openelectives':openelectives,'professionalelectives':professionalelectives})

def checkelective(request):
    oe1,oe2,oe3=request.POST.get('OpenElective1'),request.POST.get('OpenElective2'),request.POST.get('OpenElective3')
    pe1,pe2,pe3=request.POST.get('ProfessionalElective1'),request.POST.get('ProfessionalElective2'),request.POST.get('ProfessionalElective3')
    electives = Elective.objects.filter(studentid=request.user.username , oe1=oe1 , oe2=oe2 , oe3=oe3 , pe1=pe1 , pe2=pe2 , pe3=pe3)
    if len(electives)==0:
        Elective.objects.create(studentid=request.user.username , oe1=oe1 , oe2=oe2 , oe3=oe3 , pe1=pe1 , pe2=pe2 , pe3=pe3)
    else:
        Elective.objects.filter(studentid=request.user.username).update(oe1=oe1 , oe2=oe2 , oe3=oe3 , pe1=pe1 , pe2=pe2 , pe3=pe3)
    return render(request,"checkelective.html")