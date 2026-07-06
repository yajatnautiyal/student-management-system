from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    conn.close()

    total_students = len(students)

    if total_students > 0:
        total_marks = sum(student[3] for student in students)
        average_marks = round(total_marks / total_students, 2)
        top_performer = max(students, key=lambda s: s[3])[1]
    else:
        average_marks = 0
        top_performer = "N/A"

    return render_template('index.html', 
                            students=students, 
                            total_students=total_students,
                            average_marks=average_marks,
                            top_performer=top_performer)

@app.route('/add-student')
def add_student_page():
    return render_template('add_student.html')

@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    student_class = request.form['class']
    marks = request.form['marks']

    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO students (name, class, marks) VALUES (?, ?, ?)',
                   (name, student_class, marks))
    conn.commit()
    conn.close()

    return redirect('/')

@app.route('/delete/<int:student_id>')
def delete_student(student_id):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/edit/<int:student_id>')
def edit_student_page(student_id):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students WHERE id = ?', (student_id,))
    student = cursor.fetchone()
    conn.close()
    return render_template('edit_student.html', student=student)

@app.route('/update/<int:student_id>', methods=['POST'])
def update_student(student_id):
    name = request.form['name']
    student_class = request.form['class']
    marks = request.form['marks']

    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE students SET name = ?, class = ?, marks = ? WHERE id = ?',
                   (name, student_class, marks, student_id))
    conn.commit()
    conn.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)