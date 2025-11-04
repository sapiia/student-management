# sms_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.db import models
from .models import Student, Course, Enrollment, Grade, Attendance
from .forms import StudentForm, CourseForm, EnrollmentForm, GradeForm, AttendanceForm, InstructorForm
from django import forms

def is_admin(user):
    return user.is_superuser

def is_teacher(user):
    return user.groups.filter(name='Teachers').exists()

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'sms_app/login.html')

@login_required
def user_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully')
    return redirect('login')

@login_required
def dashboard(request):
    total_students = Student.objects.count()
    total_courses = Course.objects.count()
    can_add_grade = is_admin(request.user) or is_teacher(request.user)

    context = {
        'total_students': total_students,
        'total_courses': total_courses,
        'can_add_grade': can_add_grade,
    }
    return render(request, 'sms_app/index.html', context)

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'sms_app/students.html', {'students': students})

@login_required
def student_detail(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    enrollments = Enrollment.objects.filter(student=student)
    return render(request, 'sms_app/student_detail.html', {
        'student': student,
        'enrollments': enrollments
    })

@login_required
@user_passes_test(is_admin)
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully')
            return redirect('student_list')
    else:
        form = StudentForm()
    
    return render(request, 'sms_app/add_student.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def edit_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully')
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'sms_app/edit_student.html', {'form': form, 'student': student})

@login_required
@user_passes_test(is_admin)
def delete_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted successfully')
        return redirect('student_list')
    
    return render(request, 'sms_app/delete_student.html', {'student': student})

@login_required
def course_list(request):
    courses = Course.objects.all()

    # Handle search and filter
    search_query = request.GET.get('search', '')
    instructor_id = request.GET.get('instructor', '')

    if search_query:
        courses = courses.filter(
            models.Q(course_code__icontains=search_query) |
            models.Q(course_name__icontains=search_query)
        )

    if instructor_id:
        courses = courses.filter(instructor_id=instructor_id)

    # Get all instructors for the filter dropdown
    instructors = User.objects.filter(groups__name='Teachers').distinct()

    return render(request, 'sms_app/courses.html', {
        'courses': courses,
        'instructors': instructors
    })

@login_required
def course_detail(request, course_code):
    course = get_object_or_404(Course, course_code=course_code)
    enrollments = Enrollment.objects.filter(course=course)
    return render(request, 'sms_app/course_detail.html', {
        'course': course,
        'enrollments': enrollments
    })

@login_required
@user_passes_test(is_admin)
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course added successfully')
            return redirect('course_list')
    else:
        form = CourseForm()
    
    return render(request, 'sms_app/add_course.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def edit_course(request, course_code):
    course = get_object_or_404(Course, course_code=course_code)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course updated successfully')
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    
    return render(request, 'sms_app/edit_course.html', {'form': form, 'course': course})

@login_required
@user_passes_test(is_admin)
def delete_course(request, course_code):
    course = get_object_or_404(Course, course_code=course_code)
    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Course deleted successfully')
        return redirect('course_list')
    
    return render(request, 'sms_app/delete_course.html', {'course': course})

@login_required
def enrollment_list(request):
    enrollments = Enrollment.objects.all()
    can_manage_enrollment = is_admin(request.user) or is_teacher(request.user)
    return render(request, 'sms_app/enrollments.html', {
        'enrollments': enrollments,
        'can_manage_enrollment': can_manage_enrollment
    })

@login_required
@user_passes_test(is_admin)
def edit_enrollment(request, enrollment_id):
    enrollment = get_object_or_404(Enrollment, id=enrollment_id)
    if request.method == 'POST':
        form = EnrollmentForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Enrollment updated successfully')
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm(instance=enrollment)

    return render(request, 'sms_app/edit_enrollment.html', {'form': form, 'enrollment': enrollment})

@login_required
@user_passes_test(is_admin)
def delete_enrollment(request, enrollment_id):
    enrollment = get_object_or_404(Enrollment, id=enrollment_id)
    if request.method == 'POST':
        enrollment.delete()
        messages.success(request, 'Enrollment deleted successfully')
        return redirect('enrollment_list')

    return render(request, 'sms_app/delete_enrollment.html', {'enrollment': enrollment})

@login_required
@user_passes_test(is_admin)
def add_enrollment(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student enrolled successfully')
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm()
    
    return render(request, 'sms_app/add_enrollment.html', {'form': form})

@login_required
def grade_list(request):
    grades = Grade.objects.all()
    can_add_grade = is_admin(request.user) or is_teacher(request.user)
    can_edit_grade = can_add_grade
    return render(request, 'sms_app/grades.html', {
        'grades': grades,
        'can_add_grade': can_add_grade,
        'can_edit_grade': can_edit_grade
    })

@login_required
@user_passes_test(lambda u: is_admin(u) or is_teacher(u))
def add_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Grade added successfully')
            return redirect('grade_list')
    else:
        form = GradeForm()

    return render(request, 'sms_app/add_grade.html', {'form': form})

@login_required
@user_passes_test(lambda u: is_admin(u) or is_teacher(u))
def edit_grade(request, grade_id):
    grade = get_object_or_404(Grade, id=grade_id)
    if request.method == 'POST':
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            messages.success(request, 'Grade updated successfully')
            return redirect('grade_list')
    else:
        form = GradeForm(instance=grade)

    return render(request, 'sms_app/edit_grade.html', {'form': form, 'grade': grade})

@login_required
@user_passes_test(lambda u: is_admin(u) or is_teacher(u))
def delete_grade(request, grade_id):
    grade = get_object_or_404(Grade, id=grade_id)
    if request.method == 'POST':
        grade.delete()
        messages.success(request, 'Grade deleted successfully')
        return redirect('grade_list')

    return render(request, 'sms_app/delete_grade.html', {'grade': grade})

@login_required
def attendance_list(request):
    attendances = Attendance.objects.all()
    can_add_attendance = is_admin(request.user) or is_teacher(request.user)
    can_edit_attendance = can_add_attendance
    return render(request, 'sms_app/attendance.html', {
        'attendances': attendances,
        'can_add_attendance': can_add_attendance,
        'can_edit_attendance': can_edit_attendance
    })

@login_required
@user_passes_test(lambda u: is_admin(u) or is_teacher(u))
def add_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Attendance recorded successfully')
            return redirect('attendance_list')
    else:
        form = AttendanceForm()

    return render(request, 'sms_app/add_attendance.html', {'form': form})

@login_required
@user_passes_test(lambda u: is_admin(u) or is_teacher(u))
def edit_attendance(request, attendance_id):
    attendance = get_object_or_404(Attendance, id=attendance_id)
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Attendance updated successfully')
            return redirect('attendance_list')
    else:
        form = AttendanceForm(instance=attendance)

    return render(request, 'sms_app/edit_attendance.html', {'form': form, 'attendance': attendance})

@login_required
@user_passes_test(lambda u: is_admin(u) or is_teacher(u))
def delete_attendance(request, attendance_id):
    attendance = get_object_or_404(Attendance, id=attendance_id)
    if request.method == 'POST':
        attendance.delete()
        messages.success(request, 'Attendance record deleted successfully')
        return redirect('attendance_list')

    return render(request, 'sms_app/delete_attendance.html', {'attendance': attendance})

@login_required
def instructor_list(request):
    # Get all users in the Teachers group
    teachers_group = Group.objects.filter(name='Teachers').first()
    if teachers_group:
        instructors = teachers_group.user_set.all()
    else:
        instructors = User.objects.none()

    # Also include superusers who might be instructors
    all_instructors = User.objects.filter(is_staff=True) | instructors
    all_instructors = all_instructors.distinct()

    # Add role information to each instructor
    instructors_with_roles = []
    for instructor in all_instructors:
        is_teacher = instructor.groups.filter(name='Teachers').exists()
        instructors_with_roles.append({
            'user': instructor,
            'is_teacher': is_teacher,
            'course_count': instructor.course_set.count()
        })

    return render(request, 'sms_app/instructors.html', {'instructors': instructors_with_roles})

@login_required
def instructor_detail(request, instructor_id):
    instructor = get_object_or_404(User, id=instructor_id)
    courses = Course.objects.filter(instructor=instructor)
    is_teacher = instructor.groups.filter(name='Teachers').exists()

    return render(request, 'sms_app/instructor_detail.html', {
        'instructor': instructor,
        'courses': courses,
        'is_teacher': is_teacher
    })

@login_required
@user_passes_test(is_admin)
def add_instructor(request):
    if request.method == 'POST':
        form = InstructorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Instructor added successfully')
            return redirect('instructor_list')
    else:
        form = InstructorForm()

    return render(request, 'sms_app/add_instructor.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def edit_instructor(request, instructor_id):
    instructor = get_object_or_404(User, id=instructor_id)
    if request.method == 'POST':
        form = InstructorForm(request.POST, instance=instructor)
        # Don't allow password change in edit
        form.fields['password'].required = False
        form.fields['password'].widget = forms.HiddenInput()
        if form.is_valid():
            user = form.save(commit=False)
            # Handle teacher group assignment
            teachers_group, created = Group.objects.get_or_create(name='Teachers')
            if form.cleaned_data['is_teacher']:
                user.groups.add(teachers_group)
            else:
                user.groups.remove(teachers_group)
            user.save()
            messages.success(request, 'Instructor updated successfully')
            return redirect('instructor_list')
    else:
        form = InstructorForm(instance=instructor)
        form.fields['password'].required = False
        form.fields['password'].widget = forms.HiddenInput()
        form.initial['is_teacher'] = instructor.groups.filter(name='Teachers').exists()

    return render(request, 'sms_app/edit_instructor.html', {'form': form, 'instructor': instructor})

@login_required
@user_passes_test(is_admin)
def delete_instructor(request, instructor_id):
    instructor = get_object_or_404(User, id=instructor_id)
    if request.method == 'POST':
        instructor.delete()
        messages.success(request, 'Instructor deleted successfully')
        return redirect('instructor_list')

    return render(request, 'sms_app/delete_instructor.html', {'instructor': instructor})