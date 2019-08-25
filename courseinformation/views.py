from django.shortcuts import render,redirect
from .models import Student,Subject,References
# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'home.html',{})

def syllabus(request):
    student=Student.objects.filter(username=request.user.username)[0]
    subjects=Subject.objects.filter(department=student.department,year=student.year,semester=student.semester)
    return render(request,'syllabus.html',{'subjects':subjects})

def reference(request):
    student=Student.objects.filter(username=request.user.username)[0]
    subjects=Subject.objects.filter(department=student.department,year=student.year,semester=student.semester)
    return render(request,'reference.html',{'subjects':subjects})

def syllabusdetail(request,id):
    student=Student.objects.filter(username=request.user.username)[0]
    subjects=Subject.objects.filter(department=student.department,year=student.year,semester=student.semester)
    subject=Subject.objects.filter(subjectid=id)[0]
    return render(request,'syllabusdetail.html',{'subjects':subjects,'subject':subject})

def referencedetails(request,id):
    student=Student.objects.filter(username=request.user.username)[0]
    subjects=Subject.objects.filter(department=student.department,year=student.year,semester=student.semester)
    reference=References.objects.filter(subjectid=id)[0]
    return render(request,'referencedetails.html',{'subjects':subjects,'reference':reference})