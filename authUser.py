import sqlite3
from flask import jsonify

def authenticate_user(email, password):
    conn = sqlite3.connect('complaint.db')  # FIX HERE
    cursor = conn.cursor()

    cursor.execute("SELECT user_id, name, email, password, role FROM users WHERE email=? AND password=?",
                   (email, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({
            "status": 200,
            "message": "Login successful",
            "user_id": user[0],
            "role": user[4]
        })
    else:
        return jsonify({
            "status": 401,
            "message": "Invalid credentials"
        })
