import datetime

from django.shortcuts import render,redirect
from .models import Student,Subject,References,Elective,Lab
from django.contrib.auth.decorators import login_required

now = datetime.datetime.now()
getsemester = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2]

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'home.html',{'student':Student.objects.get(username=request.user.username)})

@login_required
def syllabus(request):
    student=Student.objects.get(username=request.user.username)
    studentyear = (now.year - student.joiningyear+1)
    studentsem = getsemester[int(now.strftime("%m"))-1]
    subjects=Subject.objects.filter(department=student.department,
                                    year=studentyear,
                                    semester=studentsem,
                                    isopenelective=False,
                                    isprofessionalelective=False)
    myelec=Elective.objects.filter(studentid=request.user.username)
    openelectives , profelectives = []  , []
    if len(myelec)>0:
        oe1,oe2,oe3,pe1,pe2,pe3=0,0,0,0,0,0
        if myelec[0].oe1!=0:
            oe1 = Subject.objects.get(subjectid=myelec[0].oe1)
        if myelec[0].oe2 != 0:
            oe2 = Subject.objects.get(subjectid=myelec[0].oe2)
        if myelec[0].oe3 != 0:
            oe3 = Subject.objects.get(subjectid=myelec[0].oe3)
        if myelec[0].pe1 != 0:
            pe1 = Subject.objects.get(subjectid=myelec[0].pe1)
        if myelec[0].pe2 != 0:
            pe2 = Subject.objects.get(subjectid=myelec[0].pe2)
        if myelec[0].pe3 != 0:
            pe3 = Subject.objects.get(subjectid=myelec[0].pe3)
        openelectives += [oe1, oe2, oe3]
        profelectives += [pe1, pe2, pe3]
    return render(request,'syllabus.html',{'subjects':subjects,
                                           'openelectives':openelectives,
                                           'profelectives':profelectives})

@login_required
def lab(request):
    student = Student.objects.get(username=request.user.username)
    studentyear = (now.year - student.joiningyear + 1)
    studentsem = getsemester[int(now.strftime("%m")) - 1]
    labs=Lab.objects.filter(department=student.department,
                                    year=studentyear,
                                    semester=studentsem)
    return render(request,"lab.html",{'labs':labs})

@login_required
def labdetail(request,id):
    student = Student.objects.get(username=request.user.username)
    studentyear = (now.year - student.joiningyear + 1)
    studentsem = getsemester[int(now.strftime("%m")) - 1]
    labs=Lab.objects.filter(department=student.department,
                                    year=studentyear,
                                    semester=studentsem)
    lab=Lab.objects.get(labid=id)
    return render(request,"lab.html",{'labs':labs,
                                      'lab':lab})


@login_required
def reference(request):
    student=Student.objects.get(username=request.user.username)
    studentyear = (now.year - student.joiningyear+1)
    studentsem = getsemester[int(now.strftime("%m")) - 1]
    subjects=Subject.objects.filter(department=student.department,
                                    year=studentyear,
                                    semester=studentsem,
                                    isopenelective=False,
                                    isprofessionalelective=False)
    myelec=Elective.objects.filter(studentid=request.user.username)
    openelectives , profelectives = []  , []
    if len(myelec)>0:
        oe1,oe2,oe3,pe1,pe2,pe3=0,0,0,0,0,0
        if myelec[0].oe1!=0:
            oe1 = Subject.objects.get(subjectid=myelec[0].oe1)
        if myelec[0].oe2 != 0:
            oe2 = Subject.objects.get(subjectid=myelec[0].oe2)
        if myelec[0].oe3 != 0:
            oe3 = Subject.objects.get(subjectid=myelec[0].oe3)
        if myelec[0].pe1 != 0:
            pe1 = Subject.objects.get(subjectid=myelec[0].pe1)
        if myelec[0].pe2 != 0:
            pe2 = Subject.objects.get(subjectid=myelec[0].pe2)
        if myelec[0].pe3 != 0:
            pe3 = Subject.objects.get(subjectid=myelec[0].pe3)
        openelectives += [oe1, oe2, oe3]
        profelectives += [pe1, pe2, pe3]
    return render(request,'reference.html',{'subjects':subjects,
                                           'openelectives':openelectives,
                                           'profelectives':profelectives})

@login_required
def syllabusdetail(request,id):
    student=Student.objects.get(username=request.user.username)
    studentyear = (now.year - student.joiningyear+1)
    studentsem = getsemester[int(now.strftime("%m")) - 1]
    subjects = Subject.objects.filter(department=student.department,
                                      year=studentyear,
                                      semester=studentsem,
                                      isopenelective=False,
                                      isprofessionalelective=False)
    myelec = Elective.objects.filter(studentid=request.user.username)
    openelectives, profelectives = [], []
    if len(myelec) > 0:
        oe1, oe2, oe3, pe1, pe2, pe3 = 0, 0, 0, 0, 0, 0
        if myelec[0].oe1 != 0:
            oe1 = Subject.objects.get(subjectid=myelec[0].oe1)
        if myelec[0].oe2 != 0:
            oe2 = Subject.objects.get(subjectid=myelec[0].oe2)
        if myelec[0].oe3 != 0:
            oe3 = Subject.objects.get(subjectid=myelec[0].oe3)
        if myelec[0].pe1 != 0:
            pe1 = Subject.objects.get(subjectid=myelec[0].pe1)
        if myelec[0].pe2 != 0:
            pe2 = Subject.objects.get(subjectid=myelec[0].pe2)
        if myelec[0].pe3 != 0:
            pe3 = Subject.objects.get(subjectid=myelec[0].pe3)
        openelectives += [oe1, oe2, oe3]
        profelectives += [pe1, pe2, pe3]
    subject=Subject.objects.filter(subjectid=id)
    if len(subject)==0:
        subject=0
    return render(request,'syllabusdetail.html',{'subjects':subjects,
                                                 'openelectives':openelectives,
                                                 'profelectives':profelectives,
                                                 'subject':subject})

@login_required
def referencedetails(request,id):
    student=Student.objects.get(username=request.user.username)
    studentyear = (now.year - student.joiningyear+1)
    studentsem = getsemester[int(now.strftime("%m")) - 1]
    subjects = Subject.objects.filter(department=student.department,
                                      year=studentyear,
                                      semester=studentsem,
                                      isopenelective=False,
                                      isprofessionalelective=False)
    myelec = Elective.objects.filter(studentid=request.user.username)
    openelectives, profelectives = [], []
    if len(myelec) > 0:
        oe1, oe2, oe3, pe1, pe2, pe3 = 0, 0, 0, 0, 0, 0
        if myelec[0].oe1 != 0:
            oe1 = Subject.objects.get(subjectid=myelec[0].oe1)
        if myelec[0].oe2 != 0:
            oe2 = Subject.objects.get(subjectid=myelec[0].oe2)
        if myelec[0].oe3 != 0:
            oe3 = Subject.objects.get(subjectid=myelec[0].oe3)
        if myelec[0].pe1 != 0:
            pe1 = Subject.objects.get(subjectid=myelec[0].pe1)
        if myelec[0].pe2 != 0:
            pe2 = Subject.objects.get(subjectid=myelec[0].pe2)
        if myelec[0].pe3 != 0:
            pe3 = Subject.objects.get(subjectid=myelec[0].pe3)
        openelectives += [oe1, oe2, oe3]
        profelectives += [pe1, pe2, pe3]
    subject = Subject.objects.filter(subjectid=id)
    reference=References.objects.filter(subjectid=id)
    if len(reference)==0:
        reference=0
    return render(request,'referencedetails.html',{'subjects':subjects,
                                                   'openelectives':openelectives,
                                                   'profelectives':profelectives,
                                                   'reference':reference,
                                                   'subject':subject})
@login_required
def myelective(request):
    openelectives=Subject.objects.filter(isopenelective=True)
    professionalelectives = Subject.objects.filter(isprofessionalelective=True)
    myelec=Elective.objects.filter(studentid=request.user.username)
    names=['None','None','None','None','None','None']
    if len(myelec)!=0:
        if myelec[0].oe1 != 0:
            names[0]=Subject.objects.filter(subjectid=myelec[0].oe1)[0].name+"(selected)"
        if myelec[0].oe2 != 0:
            names[1]=Subject.objects.filter(subjectid=myelec[0].oe2)[0].name+"(selected)"
        if myelec[0].oe3 != 0:
            names[2]=Subject.objects.filter(subjectid=myelec[0].oe3)[0].name+"(selected)"
        if myelec[0].pe1 != 0:
            names[3]=Subject.objects.filter(subjectid=myelec[0].pe1)[0].name+"(selected)"
        if myelec[0].pe2 != 0:
            names[4]=Subject.objects.filter(subjectid=myelec[0].pe2)[0].name+"(selected)"
        if myelec[0].pe3 != 0:
            names[5]=Subject.objects.filter(subjectid=myelec[0].pe3)[0].name+"(selected)"
    return render(request, 'myelective.html',{'openelectives': openelectives,
                                              'professionalelectives': professionalelectives,
                                              'myelec':myelec,
                                              'names':names})
@login_required
def checkelective(request):
    oe1,oe2,oe3=request.POST.get('OpenElective1'),request.POST.get('OpenElective2'),request.POST.get('OpenElective3')
    pe1,pe2,pe3=request.POST.get('ProfessionalElective1'),request.POST.get('ProfessionalElective2'),request.POST.get('ProfessionalElective3')
    if oe1 is '':
        oe1='0'
    if oe2 is '':
        oe2='0'
    if oe3 is '':
        oe3='0'
    if pe1 is '':
        pe1='0'
    if pe2 is '':
        pe2='0'
    if pe3 is '':
        pe3='0'
    electives = Elective.objects.filter(studentid=request.user.username)
    if len(electives)==0:
        Elective.objects.create(studentid=request.user.username , oe1=oe1 , oe2=oe2 , oe3=oe3 , pe1=pe1 , pe2=pe2 , pe3=pe3)
    else:
        Elective.objects.filter(studentid=request.user.username).update(oe1=oe1 , oe2=oe2 , oe3=oe3 , pe1=pe1 , pe2=pe2 , pe3=pe3)

    return render(request,"checkelective.html")