"""
Project Verification Script
Checks if all required files and configurations are in place
"""

import os
import sys
from pathlib import Path

# Color codes for terminal output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def check_file(filepath, description):
    """Check if a file exists"""
    if os.path.exists(filepath):
        print(f"{GREEN}✓{RESET} {description}")
        return True
    else:
        print(f"{RED}✗{RESET} {description} - MISSING: {filepath}")
        return False

def check_directory(dirpath, description):
    """Check if a directory exists"""
    if os.path.isdir(dirpath):
        print(f"{GREEN}✓{RESET} {description}")
        return True
    else:
        print(f"{RED}✗{RESET} {description} - MISSING: {dirpath}")
        return False

def main():
    print(f"\n{BLUE}{'='*60}{RESET}")
    print(f"{BLUE}Student Management System - Project Verification{RESET}")
    print(f"{BLUE}{'='*60}{RESET}\n")
    
    all_checks = []
    
    # Check core Django files
    print(f"{YELLOW}1. Core Django Files{RESET}")
    all_checks.append(check_file('manage.py', 'manage.py'))
    all_checks.append(check_file('student_management/settings.py', 'Settings'))
    all_checks.append(check_file('student_management/urls.py', 'Main URLs'))
    all_checks.append(check_file('student_management/wsgi.py', 'WSGI'))
    
    # Check app files
    print(f"\n{YELLOW}2. App Files (sms_app){RESET}")
    all_checks.append(check_file('sms_app/models.py', 'Models'))
    all_checks.append(check_file('sms_app/views.py', 'Views'))
    all_checks.append(check_file('sms_app/urls.py', 'App URLs'))
    all_checks.append(check_file('sms_app/forms.py', 'Forms'))
    all_checks.append(check_file('sms_app/admin.py', 'Admin'))
    
    # Check template directory structure
    print(f"\n{YELLOW}3. Template Directory{RESET}")
    all_checks.append(check_directory('sms_app/templates', 'Templates directory'))
    all_checks.append(check_directory('sms_app/templates/sms_app', 'App templates subdirectory'))
    
    # Check all required templates
    print(f"\n{YELLOW}4. Template Files (19 required){RESET}")
    templates = [
        'base.html',
        'login.html',
        'index.html',
        'students.html',
        'student_detail.html',
        'add_student.html',
        'edit_student.html',
        'delete_student.html',
        'courses.html',
        'course_detail.html',
        'add_course.html',
        'edit_course.html',
        'delete_course.html',
        'enrollments.html',
        'add_enrollment.html',
        'grades.html',
        'add_grade.html',
        'attendance.html',
        'add_attendance.html',
    ]
    
    for template in templates:
        filepath = f'sms_app/templates/sms_app/{template}'
        all_checks.append(check_file(filepath, f'  {template}'))
    
    # Check setup files
    print(f"\n{YELLOW}5. Setup and Documentation Files{RESET}")
    all_checks.append(check_file('setup_test_data.py', 'Test data setup script'))
    all_checks.append(check_file('PROJECT_STATUS.md', 'Project status documentation'))
    all_checks.append(check_file('QUICK_START.md', 'Quick start guide'))
    
    # Check for database file (SQLite) or configuration
    print(f"\n{YELLOW}6. Database Configuration{RESET}")
    try:
        with open('student_management/settings.py', 'r') as f:
            content = f.read()
            if 'mysql' in content.lower():
                print(f"{GREEN}✓{RESET} MySQL database configured")
                all_checks.append(True)
            elif 'sqlite' in content.lower():
                print(f"{GREEN}✓{RESET} SQLite database configured")
                all_checks.append(True)
            else:
                print(f"{YELLOW}⚠{RESET} Database configuration found but type unclear")
                all_checks.append(True)
    except Exception as e:
        print(f"{RED}✗{RESET} Could not verify database configuration: {e}")
        all_checks.append(False)
    
    # Summary
    print(f"\n{BLUE}{'='*60}{RESET}")
    total_checks = len(all_checks)
    passed_checks = sum(all_checks)
    failed_checks = total_checks - passed_checks
    
    print(f"\n{BLUE}Summary:{RESET}")
    print(f"  Total Checks: {total_checks}")
    print(f"  {GREEN}Passed: {passed_checks}{RESET}")
    print(f"  {RED}Failed: {failed_checks}{RESET}")
    
    if failed_checks == 0:
        print(f"\n{GREEN}{'='*60}{RESET}")
        print(f"{GREEN}✓ ALL CHECKS PASSED! Project is ready to run.{RESET}")
        print(f"{GREEN}{'='*60}{RESET}")
        print(f"\n{BLUE}Next Steps:{RESET}")
        print(f"  1. Make sure MySQL is running (XAMPP)")
        print(f"  2. Run: {YELLOW}python manage.py migrate{RESET}")
        print(f"  3. Run: {YELLOW}python manage.py shell < setup_test_data.py{RESET}")
        print(f"  4. Run: {YELLOW}python manage.py runserver{RESET}")
        print(f"  5. Open: {YELLOW}http://127.0.0.1:8000/{RESET}")
        print(f"\n{BLUE}Login Credentials (after setup):{RESET}")
        print(f"  Admin: username={YELLOW}admin{RESET}, password={YELLOW}admin123{RESET}")
        print(f"  Teacher: username={YELLOW}teacher1{RESET}, password={YELLOW}teacher123{RESET}")
    else:
        print(f"\n{RED}{'='*60}{RESET}")
        print(f"{RED}✗ SOME CHECKS FAILED! Please fix the issues above.{RESET}")
        print(f"{RED}{'='*60}{RESET}")
    
    print()
    return 0 if failed_checks == 0 else 1

if __name__ == '__main__':
    sys.exit(main())

