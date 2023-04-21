from django.db import models

# Create your models here.
class Student(models.Model):
    
    name = models.CharField(max_length=300, null=True)
    grade = models.CharField(max_length=10, null=True)
    number = models.CharField(max_length=15, null=True)
    address = models.TextField(max_length=500, null=True)
    date_of_birth = models.DateField(null=True)

    def __str__(self):
        return f"{self.name}"
    
class Teacher(models.Model):
    
    name = models.CharField(max_length=300, null=True)
    department = models.CharField(max_length=300)
    email = models.CharField(max_length=50)
    number = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=500, null=True)

    def __str__(self):
        return f"{self.name}"
    

class Subject(models.Model):
    subject = models.CharField(max_length=50)

    def __str__(self):
        return (f"{self.subject}")


class Result(models.Model):
    student = models.ForeignKey(Student, related_name="student", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name="subjects", on_delete=models.CASCADE)
    marks = models.IntegerField()

    class Meta:

        unique_together = ['student', 'subject']

    def __str__(self):
        return (f'{self.student} - {self.subject} : {self.marks}')


