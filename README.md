#  Student Management System

A full-stack web application built with Flask and SQLite to manage student records — including adding, viewing, searching, editing, and deleting students, with a live analytics dashboard.

## Features

- **Add Students** — Store student name, department/course, and CGPA
- **View Dashboard** — Real-time stats: total students, average CGPA, and top performer
- **Search** — Filter students by name or department instantly
- **Edit Records** — Update any student's details via a pre-filled form
- **Delete Records** — Remove students from the database
- **Modern UI** — Dark graphite theme with glassmorphism design

##  Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite
- **Frontend:** HTML, CSS (custom glassmorphism styling), Jinja2 templating

##  How to Run Locally

1. Clone the repository
```bash
   git clone https://github.com/yajatnautiyal/student-management-system.git
   cd student-management-system
```

2. Install Flask
```bash
   pip install flask
```

3. Initialize the database
```bash
   python database.py
```

4. Run the app
```bash
   python app.py
```

5. Open your browser and go to

http://127.0.0.1:5000

## Project Structure
student_management/
│
├── app.py                  # Main Flask application
├── database.py              # Database initialization script
├── students.db               # SQLite database (auto-generated)
├── templates/
│   ├── index.html            # Homepage with dashboard & search
│   ├── add_student.html      # Add student form
│   └── edit_student.html     # Edit student form
└── README.md

##  Future Improvements

- User authentication (login system)
- Export student data to CSV/PDF
- Pagination for large student lists

##  Author

**Yajat Nautiyal**  
[GitHub](https://github.com/yajatnautiyal)