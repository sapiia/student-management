"""
Test script to verify course list and course detail pages
"""

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_management.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User

def test_course_pages():
    print("=" * 60)
    print("Testing Course Pages - Student Management System")
    print("=" * 60)

    # Create test client
    client = Client()

    # Create a test user if needed
    if not User.objects.filter(username='testuser').exists():
        User.objects.create_user(username='testuser', password='testpass')

    user = User.objects.get(username='testuser')
    client.force_login(user)

    # Test course list page
    print("Testing course list page...")
    try:
        response = client.get('/courses/', HTTP_HOST='127.0.0.1:8000')
        if response.status_code == 200:
            print("SUCCESS: Course list page loads successfully (status: 200)")
            if 'CS102' in response.content.decode():
                print("SUCCESS: Course CS102 appears in the course list")
            else:
                print("ERROR: Course CS102 not found in course list")
        else:
            print("ERROR: Course list page failed (status: {})".format(response.status_code))
    except Exception as e:
        print("ERROR: Failed to test course list: {}".format(e))

    # Test course detail page
    print("\nTesting course detail page...")
    try:
        response = client.get('/courses/CS102/', HTTP_HOST='127.0.0.1:8000')
        if response.status_code == 200:
            print("SUCCESS: Course detail page loads successfully (status: 200)")
            content = response.content.decode()
            if 'Data Structures' in content:
                print("SUCCESS: Course name 'Data Structures' appears on detail page")
            else:
                print("ERROR: Course name not found on detail page")
        else:
            print("ERROR: Course detail page failed (status: {})".format(response.status_code))
    except Exception as e:
        print("ERROR: Failed to test course detail: {}".format(e))

    print("=" * 60)
    print("Testing completed!")
    print("You can manually test at: http://127.0.0.1:8000/courses/")
    print("=" * 60)

if __name__ == '__main__':
    test_course_pages()