import sqlite3

def createtable():
    conn = sqlite3.connect('complaint.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users(
                        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        email TEXT UNIQUE,
                        password TEXT,
                        role TEXT,
                        department TEXT,
                        phone TEXT
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS complaints(
                        complaint_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        title TEXT,
                        description TEXT,
                        status TEXT,
                        admin_remark TEXT,
                        FOREIGN KEY(user_id) REFERENCES users(user_id)
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS feedback(
                        feedback_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        feedback TEXT,
                        rating INTEGER,
                        FOREIGN KEY(user_id) REFERENCES users(user_id)
                    )''')

    conn.commit()
    conn.close()
