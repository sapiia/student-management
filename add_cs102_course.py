"""
Script to add CS102: Data Structures course to the Student Management System
"""

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_management.settings')
django.setup()

from django.contrib.auth.models import User
from sms_app.models import Course

print("=" * 60)
print("Adding Course CS102 - Student Management System")
print("=" * 60)

# Course data
course_data = {
    'course_code': 'CS102',
    'course_name': 'Data Structures',
    'description': 'Learn about data structures and algorithms',
    'credits': 4
}

# Try to get an instructor
instructor = User.objects.filter(is_staff=True).first()

# Create the course
try:
    # Check if course already exists
    if Course.objects.filter(course_code=course_data['course_code']).exists():
        print("Course {} already exists!".format(course_data['course_code']))
        course = Course.objects.get(course_code=course_data['course_code'])
        print("Existing Course Details:")
    else:
        course = Course.objects.create(
            course_code=course_data['course_code'],
            course_name=course_data['course_name'],
            description=course_data['description'],
            credits=course_data['credits'],
            instructor=instructor
        )
        print("Course created successfully!")
        print("New Course Details:")

    print("  Code: {}".format(course.course_code))
    print("  Name: {}".format(course.course_name))
    print("  Description: {}".format(course.description))
    print("  Credits: {}".format(course.credits))
    print("  Instructor: {}".format(course.instructor.username if course.instructor else 'Not assigned'))

    print("=" * 60)
    print("View all courses at: http://127.0.0.1:8000/courses/")
    print("View this course at: http://127.0.0.1:8000/courses/{}/".format(course.course_code))
    print("=" * 60)

except Exception as e:
    print("Error: {}".format(e))
    import traceback
    traceback.print_exc()