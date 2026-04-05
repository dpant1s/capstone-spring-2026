from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)
DATABASE = "medication.db"


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS medication_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            medication_name TEXT NOT NULL,
            taken_time TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def home():
    return jsonify({
        "message": "Medication Adherence MVP Backend is running"
    })


@app.route("/log_medication", methods=["POST"])
def log_medication():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    user_id = data.get("user_id")
    medication_name = data.get("medication_name")
    taken_time = data.get("taken_time")
    status = data.get("status")

    if not user_id or not medication_name or not status:
        return jsonify({
            "error": "user_id, medication_name, and status are required"
        }), 400

    if not taken_time:
        taken_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO medication_logs (user_id, medication_name, taken_time, status)
        VALUES (?, ?, ?, ?)
    """, (user_id, medication_name, taken_time, status))

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Medication log saved successfully"
    }), 201


@app.route("/history/<user_id>", methods=["GET"])
def get_history(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM medication_logs
        WHERE user_id = ?
        ORDER BY taken_time DESC
    """, (user_id,))

    rows = cursor.fetchall()
    conn.close()

    history = []
    for row in rows:
        history.append({
            "id": row["id"],
            "user_id": row["user_id"],
            "medication_name": row["medication_name"],
            "taken_time": row["taken_time"],
            "status": row["status"]
        })

    return jsonify(history), 200


if __name__ == "__main__":
    create_table()
    app.run(debug=True)
