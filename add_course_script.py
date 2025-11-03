"""
Script to add a new course to the Student Management System
"""

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_management.settings')
django.setup()

from django.contrib.auth.models import User
from sms_app.models import Course

print("=" * 60)
print("Add New Course - Student Management System")
print("=" * 60)

# Get course details
course_code = input("\nEnter Course Code (e.g., CS102): ").strip()
course_name = input("Enter Course Name (e.g., Data Structures): ").strip()
description = input("Enter Course Description: ").strip()
credits = input("Enter Credits (default 3): ").strip() or "3"

# Get instructor
print("\nAvailable Instructors:")
instructors = User.objects.filter(is_staff=True)
if instructors.exists():
    for idx, instructor in enumerate(instructors, 1):
        print(f"  {idx}. {instructor.username} - {instructor.get_full_name() or 'No name'}")
    
    instructor_choice = input("\nSelect instructor number (or press Enter to skip): ").strip()
    
    if instructor_choice and instructor_choice.isdigit():
        instructor_idx = int(instructor_choice) - 1
        if 0 <= instructor_idx < len(instructors):
            instructor = instructors[instructor_idx]
        else:
            instructor = None
    else:
        instructor = None
else:
    print("  No instructors found. Course will be created without an instructor.")
    instructor = None

# Create the course
try:
    course = Course.objects.create(
        course_code=course_code,
        course_name=course_name,
        description=description,
        credits=int(credits),
        instructor=instructor
    )
    
    print("\n" + "=" * 60)
    print("✓ Course created successfully!")
    print("=" * 60)
    print(f"\nCourse Details:")
    print(f"  Code: {course.course_code}")
    print(f"  Name: {course.course_name}")
    print(f"  Description: {course.description}")
    print(f"  Credits: {course.credits}")
    print(f"  Instructor: {course.instructor or 'Not assigned'}")
    print("\nYou can view this course at: http://127.0.0.1:8000/courses/")
    print("=" * 60)
    
except Exception as e:
    print(f"\n✗ Error creating course: {e}")

