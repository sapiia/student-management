# sms_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Student URLs
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/<str:student_id>/', views.student_detail, name='student_detail'),
    path('students/<str:student_id>/edit/', views.edit_student, name='edit_student'),
    path('students/<str:student_id>/delete/', views.delete_student, name='delete_student'),

    # Course URLs
    path('courses/', views.course_list, name='course_list'),
    path('courses/add/', views.add_course, name='add_course'),
    path('courses/<str:course_code>/', views.course_detail, name='course_detail'),
    path('courses/<str:course_code>/edit/', views.edit_course, name='edit_course'),
    path('courses/<str:course_code>/delete/', views.delete_course, name='delete_course'),
    
    # Enrollment URLs
    path('enrollments/', views.enrollment_list, name='enrollment_list'),
    path('enrollments/add/', views.add_enrollment, name='add_enrollment'),
    path('enrollments/<int:enrollment_id>/edit/', views.edit_enrollment, name='edit_enrollment'),
    path('enrollments/<int:enrollment_id>/delete/', views.delete_enrollment, name='delete_enrollment'),
    
    # Grade URLs
    path('grades/', views.grade_list, name='grade_list'),
    path('grades/add/', views.add_grade, name='add_grade'),
    path('grades/<int:grade_id>/edit/', views.edit_grade, name='edit_grade'),
    path('grades/<int:grade_id>/delete/', views.delete_grade, name='delete_grade'),
    
    # Attendance URLs
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance/add/', views.add_attendance, name='add_attendance'),
    path('attendance/<int:attendance_id>/edit/', views.edit_attendance, name='edit_attendance'),
    path('attendance/<int:attendance_id>/delete/', views.delete_attendance, name='delete_attendance'),

    # Instructor URLs
    path('instructors/', views.instructor_list, name='instructor_list'),
    path('instructors/add/', views.add_instructor, name='add_instructor'),
    path('instructors/<int:instructor_id>/', views.instructor_detail, name='instructor_detail'),
    path('instructors/<int:instructor_id>/edit/', views.edit_instructor, name='edit_instructor'),
    path('instructors/<int:instructor_id>/delete/', views.delete_instructor, name='delete_instructor'),
]