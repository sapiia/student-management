"""
Setup script to create test data for the Student Management System
Run this script with: python manage.py shell < setup_test_data.py
"""

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_management.settings')
django.setup()

from django.contrib.auth.models import User, Group
from sms_app.models import Student, Course, Enrollment, Grade, Attendance
from datetime import date, timedelta

print("=" * 50)
print("Setting up test data for Student Management System")
print("=" * 50)

# Create superuser if not exists
print("\n1. Creating superuser...")
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("   ✓ Superuser 'admin' created (password: admin123)")
else:
    print("   ✓ Superuser 'admin' already exists")

# Create Teachers group
print("\n2. Creating Teachers group...")
teachers_group, created = Group.objects.get_or_create(name='Teachers')
if created:
    print("   ✓ Teachers group created")
else:
    print("   ✓ Teachers group already exists")

# Create a teacher user
print("\n3. Creating teacher user...")
if not User.objects.filter(username='teacher1').exists():
    teacher = User.objects.create_user('teacher1', 'teacher1@example.com', 'teacher123')
    teacher.groups.add(teachers_group)
    print("   ✓ Teacher 'teacher1' created (password: teacher123)")
else:
    teacher = User.objects.get(username='teacher1')
    print("   ✓ Teacher 'teacher1' already exists")

# Create sample students
print("\n4. Creating sample students...")
students_data = [
    {
        'student_id': 'S001',
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com',
        'phone': '1234567890',
        'address': '123 Main St, City',
        'date_of_birth': date(2000, 1, 15)
    },
    {
        'student_id': 'S002',
        'first_name': 'Jane',
        'last_name': 'Smith',
        'email': 'jane.smith@example.com',
        'phone': '0987654321',
        'address': '456 Oak Ave, Town',
        'date_of_birth': date(2001, 3, 22)
    },
    {
        'student_id': 'S003',
        'first_name': 'Mike',
        'last_name': 'Johnson',
        'email': 'mike.johnson@example.com',
        'phone': '5551234567',
        'address': '789 Pine Rd, Village',
        'date_of_birth': date(1999, 7, 10)
    },
]

for student_data in students_data:
    student, created = Student.objects.get_or_create(
        student_id=student_data['student_id'],
        defaults=student_data
    )
    if created:
        print(f"   ✓ Student {student.student_id} - {student.first_name} {student.last_name} created")
    else:
        print(f"   ✓ Student {student.student_id} already exists")

# Create sample courses
print("\n5. Creating sample courses...")
courses_data = [
    {
        'course_code': 'CS101',
        'course_name': 'Introduction to Computer Science',
        'description': 'Basic concepts of computer science and programming',
        'credits': 3,
        'instructor': teacher
    },
    {
        'course_code': 'MATH201',
        'course_name': 'Calculus I',
        'description': 'Differential and integral calculus',
        'credits': 4,
        'instructor': teacher
    },
    {
        'course_code': 'ENG101',
        'course_name': 'English Composition',
        'description': 'Academic writing and composition',
        'credits': 3,
        'instructor': teacher
    },
]

for course_data in courses_data:
    course, created = Course.objects.get_or_create(
        course_code=course_data['course_code'],
        defaults=course_data
    )
    if created:
        print(f"   ✓ Course {course.course_code} - {course.course_name} created")
    else:
        print(f"   ✓ Course {course.course_code} already exists")

# Create enrollments
print("\n6. Creating enrollments...")
students = Student.objects.all()
courses = Course.objects.all()

enrollment_count = 0
for student in students:
    for course in courses[:2]:  # Enroll each student in first 2 courses
        enrollment, created = Enrollment.objects.get_or_create(
            student=student,
            course=course
        )
        if created:
            enrollment_count += 1
            print(f"   ✓ Enrolled {student.first_name} {student.last_name} in {course.course_name}")

if enrollment_count == 0:
    print("   ✓ Enrollments already exist")

# Create sample grades
print("\n7. Creating sample grades...")
enrollments = Enrollment.objects.all()
grades_list = ['A', 'B', 'C', 'A', 'B', 'A']

grade_count = 0
for i, enrollment in enumerate(enrollments):
    grade_value = grades_list[i % len(grades_list)]
    grade, created = Grade.objects.get_or_create(
        enrollment=enrollment,
        semester='Fall',
        academic_year='2023-2024',
        defaults={'grade': grade_value}
    )
    if created:
        grade_count += 1
        print(f"   ✓ Grade {grade_value} assigned to {enrollment.student.first_name} for {enrollment.course.course_name}")

if grade_count == 0:
    print("   ✓ Grades already exist")

# Create sample attendance
print("\n8. Creating sample attendance records...")
attendance_count = 0
today = date.today()

for enrollment in enrollments[:3]:  # Create attendance for first 3 enrollments
    for i in range(5):  # 5 days of attendance
        attendance_date = today - timedelta(days=i)
        status = 'P' if i % 3 != 0 else 'A'  # Present most days, absent occasionally
        
        attendance, created = Attendance.objects.get_or_create(
            enrollment=enrollment,
            date=attendance_date,
            defaults={'status': status}
        )
        if created:
            attendance_count += 1

if attendance_count > 0:
    print(f"   ✓ Created {attendance_count} attendance records")
else:
    print("   ✓ Attendance records already exist")

# Summary
print("\n" + "=" * 50)
print("SETUP COMPLETE!")
print("=" * 50)
print("\nSummary:")
print(f"  • Students: {Student.objects.count()}")
print(f"  • Courses: {Course.objects.count()}")
print(f"  • Enrollments: {Enrollment.objects.count()}")
print(f"  • Grades: {Grade.objects.count()}")
print(f"  • Attendance Records: {Attendance.objects.count()}")
print("\nLogin Credentials:")
print("  Admin: username='admin', password='admin123'")
print("  Teacher: username='teacher1', password='teacher123'")
print("\nYou can now run the server with: python manage.py runserver")
print("=" * 50)

