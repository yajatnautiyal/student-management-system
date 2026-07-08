import psycopg2
import os

def get_connection():
    database_url = os.environ.get('DATABASE_URL')
    conn = psycopg2.connect(database_url)
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
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