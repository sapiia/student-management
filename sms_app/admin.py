# sms_app/admin.py
from django.contrib import admin
from .models import Student, Course, Enrollment, Grade, Attendance

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'first_name', 'last_name', 'email', 'enrollment_date')
    search_fields = ('student_id', 'first_name', 'last_name', 'email')
    list_filter = ('enrollment_date',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'course_name', 'credits', 'instructor')
    search_fields = ('course_code', 'course_name')
    list_filter = ('credits',)

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrollment_date')
    list_filter = ('enrollment_date', 'course')

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'grade', 'semester', 'academic_year')
    list_filter = ('semester', 'academic_year', 'grade')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'date', 'status')
    list_filter = ('date', 'status')