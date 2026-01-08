import sqlite3
from flask import jsonify

def updateComplaintStatus(complaint_id, status, admin_remark):
    try:
        conn = sqlite3.connect('complaint.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE complaints SET status=?, admin_remark=? WHERE complaint_id=?",
                       (status, admin_remark, complaint_id))
        conn.commit()
        conn.close()
        return jsonify({"message": "Complaint updated successfully", "status": 200})
    except Exception as e:
        return jsonify({"message": str(e), "status": 500})

    finally:
        if conn:
            conn.close()
