from flask import Flask
import sqlite3

app=Flask(__name__)

import os
import sqlite3

def init_db():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_folder = os.path.join(base_dir, 'data')
    db_path = os.path.join(db_folder, 'database.db')

    # Ensure the folder exists
    if not os.path.exists(db_folder):
        os.makedirs(db_folder)

    # Try to write a test file to make sure it's writable
    test_file_path = os.path.join(db_folder, "test.txt")
    with open(test_file_path, "w") as f:
        f.write("test")

    # Connect to the database
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return 'Flask is working, DB initialized!'

if __name__=='__main__':
    init_db()
    app.run(debug=True)
    