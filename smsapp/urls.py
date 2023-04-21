from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('studentslist/', views.studentlist, name='studentlist'),
    path('addstudent/', views.addstudent, name='addstudent'),
    path('studentprofile/<int:sid>', views.studentprofile, name='studentprofile'),
    path('subjectslist/', views.subjectslist, name='subjectslist'),
    path('addsubject/', views.addsubject, name='addsubject'),
    path('delete/<int:sid>', views.delete, name='delete'),
    path('subdelete/<int:sid>', views.subdelete, name='subdelete'),
    path('resultdelete/<int:sid>', views.resultdelete, name='resultdelete'),
    path('addresult/', views.addresult, name='addstudent'),
    path('student/result/<int:sid>', views.viewresult, name='viewresult'),
    path('resultrank/', views.resultrank, name='resultrank')
]
