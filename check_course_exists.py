"""
Check if a course already exists in the Student Management System
"""

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_management.settings')
django.setup()

from sms_app.models import Course

# Check if CS102 exists
course_code = 'CS102'
try:
    course = Course.objects.filter(course_code=course_code).first()
    if course:
        print("SUCCESS: Course {} found!".format(course_code))
        print("Course Details:")
        print("  Code: {}".format(course.course_code))
        print("  Name: {}".format(course.course_name))
        print("  Credits: {}".format(course.credits))
        print("  Instructor: {}".format(course.instructor or 'Not assigned'))
    else:
        print("Course {} does not exist in the database.".format(course_code))

except Exception as e:
    print("Error checking course: {}".format(e))
    import traceback
    traceback.print_exc()