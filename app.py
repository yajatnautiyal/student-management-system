from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-later'

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin123'

@app.route('/')
def home():
    search_query = request.args.get('search', '')
    performance_filter = request.args.get('performance', '')

    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    if search_query:
        cursor.execute('''
            SELECT * FROM students 
            WHERE name LIKE ? OR department LIKE ?
        ''', ('%' + search_query + '%', '%' + search_query + '%'))
    else:
        cursor.execute('SELECT * FROM students')

    all_students = cursor.fetchall()
    conn.close()

    students_with_performance = []
    for student in all_students:
        cgpa = student[3]
        if cgpa >= 7.5:
            performance = "Above Average"
        elif cgpa >= 5.5:
            performance = "Average"
        else:
            performance = "Below Average"
        students_with_performance.append(student + (performance,))

    if performance_filter:
        students = [s for s in students_with_performance if s[4] == performance_filter]
    else:
        students = students_with_performance

    total_students = len(students)

    if total_students > 0:
        total_cgpa = sum(student[3] for student in students)
        average_cgpa = round(total_cgpa / total_students, 2)
        top_performer = max(students, key=lambda s: s[3])[1]
    else:
        average_cgpa = 0
        top_performer = "N/A"

    return render_template('index.html', 
                            students=students, 
                            total_students=total_students,
                            average_cgpa=average_cgpa,
                            top_performer=top_performer,
                            search_query=search_query,
                            performance_filter=performance_filter,
                            logged_in=session.get('logged_in', False))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['logged_in'] = True
            return redirect('/')
        else:
            error = "Invalid username or password"
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect('/')

@app.route('/add-student')
def add_student_page():
    if not session.get('logged_in'):
        return redirect('/login')
    return render_template('add_student.html')

@app.route('/add', methods=['POST'])
def add_student():
    if not session.get('logged_in'):
        return redirect('/login')

    name = request.form['name']
    department = request.form['department']
    cgpa = request.form['cgpa']

    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO students (name, department, cgpa) VALUES (?, ?, ?)',
                   (name, department, cgpa))
    conn.commit()
    conn.close()

    return redirect('/')

@app.route('/delete/<int:student_id>')
def delete_student(student_id):
    if not session.get('logged_in'):
        return redirect('/login')

    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/edit/<int:student_id>')
def edit_student_page(student_id):
    if not session.get('logged_in'):
        return redirect('/login')

    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students WHERE id = ?', (student_id,))
    student = cursor.fetchone()
    conn.close()
    return render_template('edit_student.html', student=student)

@app.route('/update/<int:student_id>', methods=['POST'])
def update_student(student_id):
    if not session.get('logged_in'):
        return redirect('/login')

    name = request.form['name']
    department = request.form['department']
    cgpa = request.form['cgpa']

    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE students SET name = ?, department = ?, cgpa = ? WHERE id = ?',
                   (name, department, cgpa, student_id))
    conn.commit()
    conn.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)