import sqlite3
from flask import jsonify

# ---------- COMMON FUNCTION ----------
def get_connection():
    conn = sqlite3.connect("complaint.db")
    conn.row_factory = sqlite3.Row   # returns dictionary-like rows
    return conn


# ---------- GET ALL USERS ----------
def get_all_users():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()

        users = [dict(row) for row in rows]

        conn.close()
        return jsonify({"status": 200, "data": users})

    except Exception as e:
        return jsonify({"status": 500, "message": str(e)})


# ---------- GET USER BY EMAIL ----------
def get_user_by_email(email):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE email=?", (email,))
        row = cursor.fetchone()

        conn.close()

        if row:
            return jsonify({"status": 200, "data": dict(row)})
        else:
            return jsonify({"status": 404, "message": "User not found"})

    except Exception as e:
        return jsonify({"status": 500, "message": str(e)})


# ---------- GET ALL COMPLAINTS ----------
def get_all_complaints():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM complaint")   # table name fixed
        rows = cursor.fetchall()

        complaints = [dict(row) for row in rows]

        conn.close()
        return jsonify({"status": 200, "data": complaints})

    except Exception as e:
        return jsonify({"status": 500, "message": str(e)})


# ---------- GET COMPLAINTS OF ONE USER ----------
def get_user_complaints(user_id):
    try:
        conn = sqlite3.connect("complaint.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM complaints WHERE user_id=?", (int(user_id),))
        rows = cursor.fetchall()

        complaints = []
        for row in rows:
            complaints.append({
                "complaint_id": row[0],
                "user_id": row[1],
                "title": row[2],
                "description": row[3],
                "status": row[4],
                "admin_remark": row[5]
            })

        conn.close()

        return jsonify({
            "status": 200,
            "message": "Success",
            "data": complaints
        })

    except Exception as e:
        return jsonify({"status": 500, "message": str(e)})

