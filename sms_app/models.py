# sms_app/models.py
from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    date_of_birth = models.DateField()
    enrollment_date = models.DateField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to='students/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"

class Course(models.Model):
    course_code = models.CharField(max_length=20, unique=True)
    course_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    credits = models.IntegerField(default=3)
    instructor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, limit_choices_to={'groups__name': 'Teachers'})
    
    def __str__(self):
        return f"{self.course_code} - {self.course_name}"

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    
    class Meta:
        unique_together = ('student', 'course')
    
    def __str__(self):
        return f"{self.student} enrolled in {self.course}"

class Grade(models.Model):
    GRADE_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('F', 'F'),
    ]
    
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    grade = models.CharField(max_length=1, choices=GRADE_CHOICES)
    semester = models.CharField(max_length=20)
    academic_year = models.CharField(max_length=9)  # Format: 2023-2024
    
    def __str__(self):
        return f"{self.enrollment.student} - {self.enrollment.course}: {self.grade}"

class Attendance(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=1, choices=[('P', 'Present'), ('A', 'Absent')])
    
    class Meta:
        unique_together = ('enrollment', 'date')
    
    def __str__(self):
        return f"{self.enrollment.student} - {self.date}: {self.status}"