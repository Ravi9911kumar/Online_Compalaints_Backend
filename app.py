from flask import Flask, jsonify, request
from createTableOperation import createtable
from addOperation import createUser, createComplaint, createFeedback
from readOperation import get_all_users, get_all_complaints, get_user_complaints
from updateOperation import updateComplaintStatus
from deleteOperation import deleteComplaint
from authUser import authenticate_user


app = Flask(__name__)
@app.teardown_appcontext
def close_connection(exception):
    try:
        import sqlite3
        sqlite3.connect('complaint.db').close()
    except Exception:
        pass



@app.route('/')
def home():
    return {"message": "Online Complaint & Feedback API Running"}

# Create user (Student/Admin)
@app.route('/createuser', methods=['POST'])
def create_user():
    try:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']
        department = request.form['department']
        phone = request.form['phone']
        return createUser(name, email, password, role, department, phone)
    except Exception as e:
        return jsonify({"message": str(e), "status": 500})

# Login user
@app.route('/login', methods=['POST'])
def login():
    try:
        email = request.form['email']
        password = request.form['password']
        return authenticate_user(email, password)
    except Exception as e:
        return jsonify({"message": str(e), "status": 500})

# Complaint operations
@app.route('/createcomplaint', methods=['POST'])
def create_complaint():
    try:
        user_id = request.form['user_id']
        title = request.form['title']
        description = request.form['description']
        return createComplaint(user_id, title, description)
    except Exception as e:
        return jsonify({"message": str(e), "status": 500})

@app.route('/getallcomplaints', methods=['GET'])
def all_complaints():
    return get_all_complaints()

@app.route('/getusercomplaints', methods=['POST'])
def user_complaints():
    user_id = request.form['user_id']
    return get_user_complaints(user_id)

@app.route('/updatecomplaint', methods=['PATCH'])
def update_complaint():
    complaint_id = request.form['complaint_id']
    status = request.form['status']
    admin_remark = request.form['admin_remark']
    return updateComplaintStatus(complaint_id, status, admin_remark)

@app.route('/deletecomplaint', methods=['DELETE'])
def delete_complaint():
    complaint_id = request.form['complaint_id']
    return deleteComplaint(complaint_id)

# Feedback
@app.route('/createfeedback', methods=['POST'])
def create_feedback():
    user_id = request.form['user_id']
    feedback = request.form['feedback']
    rating = request.form['rating']
    return createFeedback(user_id, feedback, rating)

@app.route('/getallusers', methods=['GET'])
def all_users():
    return get_all_users()

@app.route("/debug_table")
def debug_table():
    try:
        import sqlite3  # Required!

        conn = sqlite3.connect("complaints.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM complaints")
        rows = cursor.fetchall()

        conn.close()

        return jsonify({"status": "success", "data": rows})

    except Exception as e:
        return jsonify({"error": str(e)})



@app.route("/debug_show_all")
def debug_show_all():
    import sqlite3
    conn = sqlite3.connect("complaint.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM complaints")
    rows = cursor.fetchall()
    conn.close()
    return {"data": rows}




if __name__ == '__main__':
    createtable()
    app.run(debug=True, threaded=True)
