# Student Management System

A comprehensive web application built with Django for managing students, courses, enrollments, grades, and attendance tracking in educational institutions.

## 🚀 Features

### User Management
- **Role-based Access Control**: Admin (full access), Teacher (limited access), and Student views
- **Secure Authentication**: Login/logout with session management
- **Permission-based UI**: Dynamic interface based on user roles

### Student Management
- Add, view, edit, and delete student records
- Profile picture upload support
- Student detail views with enrollment history
- Unique student ID system

### Course Management
- Course creation with instructor assignment
- Course search and filtering by instructor
- Course detail views with enrolled students
- Credit system for course management

### Enrollment System
- Student-course enrollment management
- Prevent duplicate enrollments
- Enrollment date tracking

### Grade Management
- Grade assignment (A, B, C, D, F) with color-coded badges
- Semester and academic year tracking
- Permission controls for grade entry

### Attendance Tracking
- Daily attendance recording
- Present/Absent status tracking
- Date-based attendance records

### Instructor Management
- Teacher role assignment
- Instructor-course associations
- Staff management interface

## 🛠️ Technology Stack

- **Backend**: Django 4.x
- **Database**: MySQL (via XAMPP)
- **Frontend**: HTML5, CSS3, Bootstrap 5, Font Awesome
- **Authentication**: Django's built-in auth system
- **File Uploads**: Django media files handling

## 📋 Prerequisites

- Python 3.8 or higher
- MySQL Server (XAMPP recommended)
- Git

## ⚡ Quick Start

### 1. Database Setup
Make sure MySQL is running (via XAMPP) and create a database:
```sql
CREATE DATABASE student_management;
```

### 2. Clone and Setup
```bash
git clone <repository-url>
cd student_management

# Create virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt
```

### 3. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Load Test Data (Optional)
```bash
python manage.py shell < setup_test_data.py
```

### 5. Run Development Server
```bash
python manage.py runserver
```

### 6. Access Application
- **URL**: http://127.0.0.1:8000/
- **Admin User**: username=`admin`, password=`admin123`
- **Teacher User**: username=`teacher1`, password=`teacher123`

## 📊 Database Schema

### Core Models

**Student**
- `student_id`: Unique identifier
- `first_name`, `last_name`: Personal information
- `email`, `phone`, `address`: Contact details
- `date_of_birth`: Birth date
- `enrollment_date`: Auto-generated enrollment timestamp
- `profile_picture`: Optional image upload

**Course**
- `course_code`: Unique course identifier
- `course_name`: Display name
- `description`: Course details
- `credits`: Credit hours
- `instructor`: Foreign key to User (limited to Teachers group)

**Enrollment**
- `student`: Foreign key to Student
- `course`: Foreign key to Course
- `enrollment_date`: Auto-generated timestamp
- Unique constraint on student-course pairs

**Grade**
- `enrollment`: Foreign key to Enrollment
- `grade`: A, B, C, D, F choices
- `semester`: Semester name
- `academic_year`: Format: "2023-2024"

**Attendance**
- `enrollment`: Foreign key to Enrollment
- `date`: Attendance date
- `status`: Present/Absent choice
- Unique constraint on enrollment-date pairs

## 🔐 User Roles & Permissions

### Admin Users (Superusers)
- Full CRUD operations on all entities
- Access to Django admin panel
- User and group management
- All teacher permissions

### Teacher Users
- View students, courses, enrollments
- Add/edit/delete grades
- Add/edit/delete attendance records
- Cannot modify student or course records

### General Users (Future Enhancement)
- View personal information
- Limited access to assigned courses

## 🎨 UI/UX Features

- **Responsive Design**: Mobile-friendly interface
- **Modern UI**: Gradient themes with Bootstrap 5
- **Icons**: Font Awesome icon library
- **Alerts**: Success/error message notifications
- **Tooltips**: Interactive help text on buttons
- **Confirmation Dialogs**: Safe delete operations
- **Search & Filter**: Course search functionality

## 📁 Project Structure

```
student_management/
├── student_management/          # Main Django project
│   ├── settings.py             # Project configuration
│   ├── urls.py                 # Main URL routing
│   ├── wsgi.py                 # WSGI configuration
│   └── asgi.py                 # ASGI configuration
├── sms_app/                    # Main application
│   ├── models.py               # Database models
│   ├── views.py                # View functions
│   ├── urls.py                 # App URL routing
│   ├── forms.py                # Django forms
│   ├── admin.py                # Admin interface
│   └── templates/sms_app/      # HTML templates
├── static/                     # Static files (CSS, JS, images)
├── media/                      # User-uploaded files
├── manage.py                   # Django management script
└── requirements.txt            # Python dependencies
```

## 🔧 Configuration

### Database Settings (settings.py)
- **Engine**: MySQL
- **Name**: student_management
- **User**: root (XAMPP default)
- **Password**: "" (empty for XAMPP)
- **Host**: localhost
- **Port**: 3306

### File Handling
- **Static Files**: `/static/` directory
- **Media Files**: `/media/` directory for uploads
- **Profile Pictures**: Stored in `media/students/`

## 🚦 API Endpoints

| Endpoint | Method | Access | Description |
|----------|--------|---------|-------------|
| `/` | GET/POST | Public | Login page |
| `/dashboard/` | GET | Auth | Main dashboard |
| `/students/` | GET | Auth | Student list |
| `/students/add/` | GET/POST | Admin | Add student |
| `/students/<id>/` | GET | Auth | Student details |
| `/courses/` | GET | Auth | Course list with search |
| `/courses/add/` | GET/POST | Admin | Add course |
| `/enrollments/` | GET | Auth | Enrollment list |
| `/grades/` | GET | Auth | Grade list |
| `/grades/add/` | GET/POST | Admin/Teacher | Add grade |
| `/attendance/` | GET | Auth | Attendance records |
| `/attendance/add/` | GET/POST | Admin/Teacher | Record attendance |
| `/admin/` | GET | Admin | Django admin panel |

## 🧪 Testing

### Running Tests
```bash
python manage.py test
```

### Manual Testing Checklist
- [ ] Login with admin credentials
- [ ] Login with teacher credentials
- [ ] Dashboard statistics display
- [ ] Student CRUD operations
- [ ] Course CRUD operations
- [ ] Enrollment management
- [ ] Grade management
- [ ] Attendance tracking
- [ ] Responsive design on mobile

## 🔍 Troubleshooting

### Common Issues

**Template Does Not Exist Error**
- Ensure templates are in `sms_app/templates/sms_app/` directory

**Database Connection Error**
- Verify MySQL server is running
- Check database credentials in `settings.py`
- Ensure database `student_management` exists

**Permission Denied Errors**
- Check user roles and group assignments
- Verify `@user_passes_test` decorators

**File Upload Issues**
- Check `MEDIA_ROOT` and `MEDIA_URL` settings
- Ensure proper file permissions on `media/` directory

## 📈 Future Enhancements

- [ ] REST API endpoints
- [ ] Student portal for self-service
- [ ] Bulk import/export functionality
- [ ] Advanced reporting and analytics
- [ ] Email notifications
- [ ] Grade calculation automation
- [ ] Course prerequisites
- [ ] Schedule management
- [ ] Mobile app companion

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Django](https://www.djangoproject.com/)
- UI powered by [Bootstrap](https://getbootstrap.com/)
- Icons from [Font Awesome](https://fontawesome.com/)
- Database support via [MySQL](https://www.mysql.com/)

---

**Ready to streamline your educational institution's management?** 🚀

For detailed setup instructions, see [QUICK_START.md](QUICK_START.md)
For project status and implementation details, see [PROJECT_STATUS.md](PROJECT_STATUS.md)