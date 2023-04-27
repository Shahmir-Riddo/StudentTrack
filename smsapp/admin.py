from django.contrib import admin
from .models import Student, Subject, Result, School

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Result)
# Register your models here.
admin.site.register(School)
