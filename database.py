import sqlite3

def init_db():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            cgpa REAL NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database and table created successfully!")

if __name__ == '__main__':
    init_db()