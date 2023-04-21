
from django.shortcuts import render, redirect
from .models import Student, Subject, Result
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.db.models import Sum, Avg, Max

def home(request):
    students = Student.objects.all()
    subjects = Subject.objects.all()
    context = {"students": len(students),
               "subjects": len(subjects)}
    return render(request, "home.html", context)

def studentlist(request):
    student = Student.objects.all()
   
    context = {'students': student}
    return render(request, "studentslist.html", context)

def addstudent(request):
    if request.method == "POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        grade = request.POST.get('grade')
        address = request.POST.get('address')
        date_of_birth = request.POST.get('birthdate')
        date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d').date()
        student_obj = Student.objects.create(name=name, number=number, grade=grade, address=address, date_of_birth=date_of_birth)
      

    return render(request, "addstudent.html")

def subjectslist(request):
    subjects = Subject.objects.all()
    context = {'subject': subjects}
    return render(request, "subjectslist.html", context)

def addsubject(request):
    if request.method == "POST":
        subject = request.POST.get('subject')
        subject_obj = Subject.objects.create(subject=subject)
    
    return render(request, "addsubject.html")

def studentprofile(request, sid):
    studen = get_object_or_404(Student, id=sid)
    print(studen)
    context = {'student': studen}
    return render(request, "studentprofile.html", context)

def addresult(request):
    if request.method == "POST":
        student = request.POST.get('student')
        subject = request.POST.get('subject')
        marks = request.POST.get('marks')
        student_obj = Student.objects.get(id=student)
        subject_obj = Subject.objects.get(id=subject)
        result_obj = Result.objects.create(student=student_obj, subject=subject_obj, marks=marks)
    result = Student.objects.all()
    subject = Subject.objects.all()
    context = {'students': result,
               'subjects': subject }
    return render(request, "addresult.html", context)

def viewresult(request, sid):

 
    student_result = Result.objects.filter(student_id=sid)
    
    student_info = get_object_or_404(Student, id=sid)

    total_marks = student_result.aggregate(total_marks = Sum('marks'))
    avg_marks = student_result.aggregate(avg_name = Avg('marks'))
    total = total_marks['total_marks']
    if total:
        gpa = total / 600 * 5
        gpa = format(gpa, ".2f")

 
        context = {'result' : student_result,
               'student': student_info,
               'total_marks': total_marks,
               'avg_marks': avg_marks,
               'gpa': gpa
            
               }
        return render(request, "result.html", context)
    context = {'result' : student_result,
               'student': student_info,
               'total_marks': total_marks,
               'avg_marks': avg_marks,
            
            
               }
    return render(request, "result.html", context)

def resultrank(request):

    student_result = Result.objects.all()
    total_marks = student_result.aggregate(total_marks = Sum('marks'))

    context = {'rank': total_marks}
    return render(request, "resultrank.html", context)

def delete(request, sid):
    student_obj = get_object_or_404(Student, id=sid)
    student_obj.delete()
    return redirect('/studentslist')

def subdelete(request, sid):
    subject_obj = get_object_or_404(Subject, id=sid)
    subject_obj.delete()
    return redirect('/subjectslist')

def resultdelete(request, sid):
    result_obj = get_object_or_404(Result, id=sid)
    result_obj.delete()
    return redirect('/studentslist')