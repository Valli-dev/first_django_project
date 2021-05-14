from django.contrib import admin
from .models import School, Student,Department,Grade,Certificate_type,Faculty

# Register your models here.

admin.site.register(School)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Grade)
admin.site.register(Certificate_type)
admin.site.register(Faculty)