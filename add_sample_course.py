"""
Quick script to add a sample course
"""

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_management.settings')
django.setup()

from django.contrib.auth.models import User
from sms_app.models import Course

print("=" * 60)
print("Adding Sample Course - Student Management System")
print("=" * 60)

# Sample course data
course_data = {
    'course_code': 'PHYS101',
    'course_name': 'Introduction to Physics',
    'description': 'Fundamental concepts of physics including mechanics, thermodynamics, and electromagnetism',
    'credits': 4
}

# Try to get an instructor
instructor = User.objects.filter(is_staff=True).first()

# Create the course
try:
    # Check if course already exists
    if Course.objects.filter(course_code=course_data['course_code']).exists():
        print(f"\n⚠ Course {course_data['course_code']} already exists!")
        course = Course.objects.get(course_code=course_data['course_code'])
        print(f"\nExisting Course Details:")
    else:
        course = Course.objects.create(
            course_code=course_data['course_code'],
            course_name=course_data['course_name'],
            description=course_data['description'],
            credits=course_data['credits'],
            instructor=instructor
        )
        print("\n✓ Course created successfully!")
        print("\nNew Course Details:")
    
    print(f"  Code: {course.course_code}")
    print(f"  Name: {course.course_name}")
    print(f"  Description: {course.description}")
    print(f"  Credits: {course.credits}")
    print(f"  Instructor: {course.instructor.username if course.instructor else 'Not assigned'}")
    
    print("\n" + "=" * 60)
    print("View all courses at: http://127.0.0.1:8000/courses/")
    print(f"View this course at: http://127.0.0.1:8000/courses/{course.course_code}/")
    print("=" * 60)
    
except Exception as e:
    print(f"\n✗ Error: {e}")
    import traceback
    traceback.print_exc()

