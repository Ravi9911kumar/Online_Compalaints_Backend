import sqlite3
from flask import jsonify

def deleteComplaint(complaint_id):
    try:
        conn = sqlite3.connect('complaint.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM complaints WHERE complaint_id=?", (complaint_id,))
        conn.commit()
        conn.close()
        return jsonify({"message": "Complaint deleted", "status": 200})
    except Exception as e:
        return jsonify({"message": str(e), "status": 500})

    finally:
        if conn:
            conn.close()
