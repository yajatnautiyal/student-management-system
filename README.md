# Student Management System

A web application for managing student records, built with Flask and PostgreSQL. Supports adding, editing, deleting, and searching students, with an admin login and a dashboard showing live stats.

**Live demo:** https://your-actual-render-link.onrender.com
(Login: use the credentials below, or just browse as a guest to see the read-only view)

## Features

- Add, edit, and delete student records (name, department, CGPA)
- Dashboard with total students, average CGPA, and top performer, updated in real time
- Search by name or department
- Filter students by performance (Above Average / Average / Below Average, based on CGPA)
- Admin login — only logged-in users can add/edit/delete; everyone else gets a read-only view
- Dark UI with a glassmorphism design

## Tech Stack

- **Backend:** Python, Flask
- **Database:** PostgreSQL
- **Frontend:** HTML, CSS, Jinja2
- **Deployment:** Render

## Running it locally

```bash
git clone https://github.com/yajatnautiyal/student-management-system.git
cd student-management-system
pip install -r requirements.txt
```

Set your database URL as an environment variable:
```bash
$env:DATABASE_URL="your_postgresql_connection_string"
```

Then initialize the database and run the app:
```bash
python database.py
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

## Project Structure

student_management/
├── app.py                # Main Flask app and routes
├── database.py            # Database table setup
├── templates/
│   ├── index.html          # Dashboard, search, student table
│   ├── add_student.html    # Add student form
│   ├── edit_student.html   # Edit student form
│   └── login.html          # Admin login
├── requirements.txt
└── Procfile

## Possible future additions

- Export student data to CSV
- Pagination for large student lists
- Password hashing for stronger authentication

## Author

Yajat Nautiyal
[GitHub](https://github.com/yajatnautiyal)