
from django.shortcuts import render, redirect
from .models import Student, Subject, Result, School, Teacher
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.contrib import messages
from django.db.models import Sum, Avg, Max, Q, Count
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/userlogin')
def home(request):
    students = Student.objects.all()
    subjects = Subject.objects.all()
    teachers = Teacher.objects.all()
    exams = Result.objects.all()
  
    try:
        school = School.objects.latest('created_at')

    except Exception as e:
        school = e

    context = {"students": len(students),
               "subjects": len(subjects),
               "teachers": len(teachers),
               "school": school,
               "exams": len(exams)
               }
    return render(request, "home.html", context)

@login_required(login_url='/userlogin')
def studentlist(request):
   

    student = Student.objects.all()
   
    context = {'students': student}
    return render(request, "studentslist.html", context)

@login_required(login_url='/userlogin')
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

@login_required(login_url='/userlogin')   
def editstudent(request, sid):
    student = Student.objects.get(id=sid)

    if request.method == "POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        grade = request.POST.get('grade')
        address = request.POST.get('address')
     
        print(name, address)
        student.name = "sawad"
        student.number = number
        student.grade = grade
        student.address = address
        student.date_of_birth = date_of_birth
        student.save()



    context = {'student': student_obj}
    return render(request, "editstudent.html", context)
#teacher
@login_required(login_url='/userlogin')
def teacherslist(request):
   

    teacher = Teacher.objects.all()
   
    context = {'teachers': teacher}
    return render(request, "teacherslist.html", context)


@login_required(login_url='/userlogin')
def addteacher(request):
    if request.method == "POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        department = request.POST.get('department')
        address = request.POST.get('address')

      
        teacher_obj = Teacher.objects.create(name=name, number=number,email=email, department=department, address=address)
      

    return render(request, "addteacher.html")

@login_required(login_url='/userlogin')
def subjectslist(request):
    subjects = Subject.objects.all()
    context = {'subject': subjects}
    return render(request, "subjectslist.html", context)

@login_required(login_url='/userlogin')
def addsubject(request):
    if request.method == "POST":
        subject = request.POST.get('subject')
        subject_obj = Subject.objects.create(subject=subject)
    
    return render(request, "addsubject.html")

@login_required(login_url='/userlogin')
def studentprofile(request, sid):
    studen = get_object_or_404(Student, id=sid)
    print(studen)
    student_ranks = Student.objects.annotate(total_marks = Sum('student__marks')).order_by('-total_marks')
    rank = -1
    for index, rank in enumerate(student_ranks, start=1):
        if rank.id == sid:
            rank = index
            print(index)
    print("_________________", rank)
    context = {'student': studen, 'rank': rank}
    return render(request, "studentprofile.html", context)

@login_required(login_url='/userlogin')   
def editstudent(request, sid):
    student = get_object_or_404(Student, id=sid)
    if request.method == "POST":
        student.name = request.POST.get('name')
        student.number = request.POST.get('number')
        student.grade = request.POST.get('grade')
        student.address = request.POST.get('address')
        student.save()

  

    context = {'student': student}
    return render(request, "editstudent.html", context)
    
@login_required(login_url='/userlogin')
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

@login_required(login_url='/userlogin')
def viewresult(request, sid):

 
    student_result = Result.objects.filter(student_id=sid)
    
    student_info = get_object_or_404(Student, id=sid)

    total_marks = student_result.aggregate(total_marks = Sum('marks'))
    avg_marks = student_result.aggregate(avg_name = Avg('marks'))
    total = total_marks['total_marks']
    grade = student_info.grade
   
    student_ranks = Student.objects.filter(grade=grade).annotate(total_marks = Sum('student__marks')).order_by('-total_marks')
    srank = -1
    for index, rank in enumerate(student_ranks, start=1):
        if rank.id == sid:
            srank = index
            
    
    if total:
        gpa = total / 600 * 5
        gpa = format(gpa, ".2f")

 
        context = {'result' : student_result,
               'student': student_info,
               'total_marks': total_marks,
               'avg_marks': avg_marks,
               'gpa': gpa,
               'rank': srank
            
               }
        return render(request, "result.html", context)
    context = {'result' : student_result,
               'student': student_info,
               'total_marks': total_marks,
               'avg_marks': avg_marks,
               'rank': rank
            
               }
    return render(request, "result.html", context)

@login_required(login_url='/userlogin')
def resultrank(request):

  

    if request.method == "POST":
        search = request.POST.get('search')
        grade_students = Student.objects.filter(grade=search)
        grade_results = grade_students.annotate(total_marks = Sum('student__marks')).order_by('-total_marks')
    
    



        context = {'search_content': grade_results}
        return render(request, "resultrank.html", context)

    grade_results = Student.objects.all().annotate(total_marks = Sum('student__marks')).order_by('-total_marks')
    

    context = {'message': 'Select A Grade To View Results',
               'search_content': grade_results}
    return render(request, "resultrank.html", context)

@login_required(login_url='/userlogin')
def search(request):
    if request.method == "GET":
        search = request.GET.get('search')
        search_results = Student.objects.filter(Q(name__icontains=search) | Q(grade__icontains=search))

    else:
        search_results = Student.objects.all()
    
    return render(request, 'search.html', context={'students': search_results})

@login_required(login_url='/userlogin')
def delete(request, sid):
    student_obj = get_object_or_404(Student, id=sid)
    student_obj.delete()
    return redirect('/studentslist')

@login_required(login_url='/userlogin')
def teacherdelete(request, sid):
    student_obj = get_object_or_404(Teacher, id=sid)
    student_obj.delete()
    return redirect('/teacherslist')

@login_required(login_url='/userlogin')
def subdelete(request, sid):
    subject_obj = get_object_or_404(Subject, id=sid)
    subject_obj.delete()
    return redirect('/subjectslist')

@login_required(login_url='/userlogin')
def resultdelete(request, sid):
    result_obj = get_object_or_404(Result, id=sid)
    result_obj.delete()
    return redirect('/studentslist')

@login_required(login_url='/userlogin')
def settings(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        short_name = request.POST.get('shortname')
        number = request.POST.get('phone')
        address = request.POST.get('address')
        school_obj = School.objects.create(name=name, short_name=short_name, number=number, address=address)

        
        
    return render(request, 'settings.html')

@login_required(login_url='/userlogin')
def signup(request):
     if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(email=email).exists():

            messages.error(request, "Email exists")

        elif User.objects.filter(username=username).exists():

            messages.info(request, "Username exists")

        else:

            user = User.objects.create_user(username=username, email=email, password= password)
            user.save()
            messages.info(request, "Registered Successfully")
            return redirect('/userlogin')

     return render(request, "signup.html")

def userlogin(request):
      
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

   
        user = authenticate(request, username=username, password=password)
        if user is not None:

            auth.login(request, user)
            return redirect("/")

    else:
        messages.info(request,  "Invalid Info")
  
    return render(request, "login.html")

@login_required(login_url='/userlogin')
def userlogout(request):
    logout(request)
    return redirect('/')