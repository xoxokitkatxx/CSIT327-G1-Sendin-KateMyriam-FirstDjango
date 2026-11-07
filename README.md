# CampusConnect

CampusConnect is a Django campus membership web application where students, instructors, and administrators can register, log in, view campus membership statistics on a dashboard, manage their personal profile, and access role-restricted administration pages.

- **Author:** Kate Myriam B. Sendin
- **Course:** CSIT327

## Features
- **Sign-Up with Feedback:** New users register with a custom user creation form and receive a dismissible Bootstrap 5 success alert upon redirect to the login page.
- **Authentication:** Session-based login and CSRF-protected POST logout.
- **Member Dashboard:** Displays the logged-in user's name, role, course, total member count, and last login date.
- **Editable User Profile:** Logged-in users can view and update their own profile information (`username`, `email`, `first_name`, `last_name`, `course`) via a class-based `UpdateView`.
- **Role-Based Admin Panel:** Custom `CustomUser` model supporting `Student`, `Instructor`, and `Administrator` roles, with an `Administrator`-restricted `/admin-panel/` view.

## Tech Stack
- **Language:** Python 3
- **Framework:** Django 6.1.2
- **Front-End Styling:** Bootstrap 5.3.3 loaded via jsDelivr CDN
- **Database:** SQLite (`db.sqlite3`)

## Project Structure
```text
Sendin_CampusConnect/
├── accounts/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── campusconnect/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── dashboard/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates/
│   ├── accounts/
│   │   └── profile.html
│   ├── dashboard/
│   │   ├── admin_panel.html
│   │   └── home.html
│   ├── registration/
│   │   ├── login.html
│   │   └── signup.html
│   └── base.html
├── manage.py
├── requirements.txt
└── README.md