from django.urls import path,include
from courseinformation import views

urlpatterns = [
    path('', views.home, name='home'),
    path(r'syllabus/', views.syllabus, name='syllabus'),
    path(r'labs/', views.lab, name='labs'),
    path(r'labs/<int:id>/', views.labdetail, name='labsdetail'),
    path(r'reference/', views.reference, name='reference'),
    path(r'syllabus/<int:id>/', views.syllabusdetail, name='syllabusdetail'),
    path(r'reference/<int:id>/', views.referencedetails , name='referencedetail'),
    path(r'myelective/', views.myelective, name='myelective'),
    path(r'myelective/checkelective', views.checkelective, name='checkelective'),
]