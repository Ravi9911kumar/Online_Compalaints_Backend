import sqlite3
from flask import jsonify




def createUser(name, email, password, role, department, phone):
    try:
        conn = sqlite3.connect('complaint.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users(name, email, password, role, department, phone) VALUES(?,?,?,?,?,?)",
                       (name, email, password, role, department, phone))
        conn.commit()
        conn.close()
        return jsonify({"message": "User created successfully", "status": 200})
    except Exception as e:
        return jsonify({"message": str(e), "status": 500})
    finally:
        if conn:
            conn.close()


def createComplaint(user_id, title, description):
    try:
        conn = sqlite3.connect('complaint.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO complaints(user_id, title, description, status) VALUES(?,?,?,?)",
                       (user_id, title, description, "Pending"))
        conn.commit()
        conn.close()
        return jsonify({"message": "Complaint submitted successfully", "status": 200})
    except Exception as e:
        return jsonify({"message": str(e), "status": 500})
    finally:
        if conn:
            conn.close()


def createFeedback(user_id, feedback, rating):
    try:
        conn = sqlite3.connect('complaint.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO feedback(user_id, feedback, rating) VALUES(?,?,?)",
                       (user_id, feedback, rating))
        conn.commit()
        conn.close()
        return jsonify({"message": "Feedback submitted successfully", "status": 200})
    except Exception as e:
        return jsonify({"message": str(e), "status": 500})
    finally:
        if conn:
            conn.close()

