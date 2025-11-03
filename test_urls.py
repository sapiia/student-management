"""
URL Pattern Test Script
Tests all URL patterns to ensure they are properly configured
"""

import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_management.settings')
django.setup()

from django.urls import reverse, NoReverseMatch

# Color codes
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def test_url(name, args=None, kwargs=None):
    """Test if a URL pattern can be reversed"""
    try:
        if args:
            url = reverse(name, args=args)
        elif kwargs:
            url = reverse(name, kwargs=kwargs)
        else:
            url = reverse(name)
        print(f"{GREEN}✓{RESET} {name:30} -> {url}")
        return True
    except NoReverseMatch as e:
        print(f"{RED}✗{RESET} {name:30} -> ERROR: {e}")
        return False

def main():
    print(f"\n{BLUE}{'='*70}{RESET}")
    print(f"{BLUE}URL Pattern Test - Student Management System{RESET}")
    print(f"{BLUE}{'='*70}{RESET}\n")
    
    results = []
    
    # Authentication URLs
    print(f"{YELLOW}Authentication URLs:{RESET}")
    results.append(test_url('login'))
    results.append(test_url('logout'))
    results.append(test_url('dashboard'))
    
    # Student URLs
    print(f"\n{YELLOW}Student URLs:{RESET}")
    results.append(test_url('student_list'))
    results.append(test_url('add_student'))
    results.append(test_url('student_detail', args=['S001']))
    results.append(test_url('edit_student', args=['S001']))
    results.append(test_url('delete_student', args=['S001']))
    
    # Course URLs
    print(f"\n{YELLOW}Course URLs:{RESET}")
    results.append(test_url('course_list'))
    results.append(test_url('add_course'))
    results.append(test_url('course_detail', args=['CS101']))
    results.append(test_url('edit_course', args=['CS101']))
    results.append(test_url('delete_course', args=['CS101']))
    
    # Enrollment URLs
    print(f"\n{YELLOW}Enrollment URLs:{RESET}")
    results.append(test_url('enrollment_list'))
    results.append(test_url('add_enrollment'))
    
    # Grade URLs
    print(f"\n{YELLOW}Grade URLs:{RESET}")
    results.append(test_url('grade_list'))
    results.append(test_url('add_grade'))
    
    # Attendance URLs
    print(f"\n{YELLOW}Attendance URLs:{RESET}")
    results.append(test_url('attendance_list'))
    results.append(test_url('add_attendance'))
    
    # Instructor URLs
    print(f"\n{YELLOW}Instructor URLs:{RESET}")
    results.append(test_url('instructor_list'))
    results.append(test_url('instructor_detail', args=[1]))
    
    # Summary
    print(f"\n{BLUE}{'='*70}{RESET}")
    total = len(results)
    passed = sum(results)
    failed = total - passed
    
    print(f"\n{BLUE}Summary:{RESET}")
    print(f"  Total URL Patterns: {total}")
    print(f"  {GREEN}Passed: {passed}{RESET}")
    print(f"  {RED}Failed: {failed}{RESET}")
    
    if failed == 0:
        print(f"\n{GREEN}{'='*70}{RESET}")
        print(f"{GREEN}✓ ALL URL PATTERNS ARE WORKING!{RESET}")
        print(f"{GREEN}{'='*70}{RESET}\n")
        return 0
    else:
        print(f"\n{RED}{'='*70}{RESET}")
        print(f"{RED}✗ SOME URL PATTERNS FAILED!{RESET}")
        print(f"{RED}{'='*70}{RESET}\n")
        return 1

if __name__ == '__main__':
    sys.exit(main())

