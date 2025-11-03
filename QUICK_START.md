# Quick Start Guide - Student Management System

## 🚀 Getting Started in 3 Steps

### Step 1: Setup Database and Run Migrations

```bash
# Navigate to project directory
cd Desktop/student_management

# Run migrations to create database tables
python manage.py makemigrations
python manage.py migrate
```

### Step 2: Create Test Data (Optional but Recommended)

```bash
# This will create admin user, teacher user, sample students, courses, etc.
python manage.py shell < setup_test_data.py
```

This creates:
- **Admin User**: username=`admin`, password=`admin123`
- **Teacher User**: username=`teacher1`, password=`teacher123`
- **3 Sample Students**: John Doe, Jane Smith, Mike Johnson
- **3 Sample Courses**: CS101, MATH201, ENG101
- **Sample Enrollments, Grades, and Attendance**

### Step 3: Run the Server

```bash
python manage.py runserver
```

Then open your browser and go to: **http://127.0.0.1:8000/**

---

## 🔐 Login Credentials

After running the setup script:

| Role | Username | Password |
|------|----------|----------|
| Admin | admin | admin123 |
| Teacher | teacher1 | teacher123 |

---

## 📱 Main Features

### For Admin Users (Full Access)
- ✅ Manage Students (Add, Edit, Delete, View)
- ✅ Manage Courses (Add, Edit, Delete, View)
- ✅ Manage Enrollments
- ✅ Manage Grades
- ✅ Manage Attendance
- ✅ Access Django Admin Panel

### For Teacher Users
- ✅ View Students and Courses
- ✅ Add Grades
- ✅ Record Attendance
- ❌ Cannot add/edit/delete students or courses

---

## 🗂️ Navigation

After logging in, use the sidebar to navigate:

1. **Dashboard** - Overview with statistics
2. **Students** - Student management
3. **Courses** - Course management
4. **Enrollments** - Student-course enrollments
5. **Grades** - Grade management
6. **Attendance** - Attendance tracking

---

## 💡 Quick Tips

### Adding a New Student
1. Click **Students** in sidebar
2. Click **Add New Student** button
3. Fill in the form (Student ID, Name, Email, etc.)
4. Optionally upload a profile picture
5. Click **Save Student**

### Enrolling a Student in a Course
1. Click **Enrollments** in sidebar
2. Click **Add New Enrollment**
3. Select a student from dropdown
4. Select a course from dropdown
5. Click **Enroll Student**

### Adding Grades
1. Click **Grades** in sidebar
2. Click **Add New Grade**
3. Select an enrollment (student-course combination)
4. Select grade (A, B, C, D, F)
5. Enter semester and academic year
6. Click **Save Grade**

### Recording Attendance
1. Click **Attendance** in sidebar
2. Click **Record Attendance**
3. Select an enrollment
4. Select date
5. Select status (Present/Absent)
6. Click **Save Attendance**

---

## 🔧 Troubleshooting

### Issue: "TemplateDoesNotExist" Error
**Solution**: All templates should be in `sms_app/templates/sms_app/` directory. This has been fixed.

### Issue: "No Student matches the given query" when accessing /students/add/
**Solution**: URL patterns have been reordered. Specific routes now come before dynamic ones.

### Issue: Can't login
**Solution**: Make sure you've run the setup script or create a superuser manually:
```bash
python manage.py createsuperuser
```

### Issue: Database connection error
**Solution**: 
1. Make sure XAMPP MySQL is running
2. Create database: `CREATE DATABASE student_management;`
3. Check credentials in `student_management/settings.py`

---

## 📊 Database Schema

### Models Overview

**Student**
- student_id (unique)
- first_name, last_name
- email, phone, address
- date_of_birth
- enrollment_date (auto)
- profile_picture (optional)

**Course**
- course_code (unique)
- course_name
- description
- credits
- instructor (foreign key to User)

**Enrollment**
- student (foreign key)
- course (foreign key)
- enrollment_date (auto)

**Grade**
- enrollment (foreign key)
- grade (A, B, C, D, F)
- semester
- academic_year

**Attendance**
- enrollment (foreign key)
- date
- status (Present/Absent)

---

## 🎨 UI Features

- **Responsive Design**: Works on desktop, tablet, and mobile
- **Modern UI**: Bootstrap 5 with custom gradient theme
- **Icons**: Font Awesome icons throughout
- **Alerts**: Success/error messages after actions
- **Tooltips**: Hover over action buttons for descriptions
- **Confirmations**: Delete actions require confirmation

---

## 📝 Manual User Creation (Alternative to Setup Script)

If you prefer to create users manually:

```bash
# Create superuser
python manage.py createsuperuser

# Then in Django shell:
python manage.py shell
```

```python
from django.contrib.auth.models import User, Group

# Create Teachers group
teachers_group = Group.objects.create(name='Teachers')

# Create a teacher user
teacher = User.objects.create_user('teacher1', 'teacher1@example.com', 'teacher123')
teacher.groups.add(teachers_group)
```

---

## 🌐 URLs Reference

| Page | URL | Access |
|------|-----|--------|
| Login | / | Public |
| Dashboard | /dashboard/ | Authenticated |
| Students List | /students/ | Authenticated |
| Add Student | /students/add/ | Admin only |
| Student Detail | /students/{id}/ | Authenticated |
| Courses List | /courses/ | Authenticated |
| Add Course | /courses/add/ | Admin only |
| Enrollments | /enrollments/ | Authenticated |
| Grades | /grades/ | Authenticated |
| Attendance | /attendance/ | Authenticated |
| Admin Panel | /admin/ | Admin only |

---

## ✅ Verification Checklist

After setup, verify these work:

- [ ] Can login with admin credentials
- [ ] Dashboard shows statistics
- [ ] Can view student list
- [ ] Can add new student (as admin)
- [ ] Can view student details
- [ ] Can view course list
- [ ] Can add new course (as admin)
- [ ] Can create enrollment
- [ ] Can add grade
- [ ] Can record attendance
- [ ] Can logout

---

## 🎯 You're All Set!

Your Student Management System is ready to use. Enjoy! 🎉

For detailed project status, see `PROJECT_STATUS.md`

