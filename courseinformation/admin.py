from django.contrib import admin
from courseinformation.models import Subject,References,Student
from django.contrib.auth.models import Group

class SubjectAdmin(admin.ModelAdmin):
    pass

class ReferencesAdmin(admin.ModelAdmin):
    pass

class StudentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Subject,SubjectAdmin)
admin.site.register(References, ReferencesAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.unregister(Group)