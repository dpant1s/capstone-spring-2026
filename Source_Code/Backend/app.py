from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)
DATABASE = "medication.db"


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            full_name TEXT NOT NULL,
            email TEXT,
            role TEXT NOT NULL CHECK(role IN ('patient', 'clinician')),
            butterfly_bucks INTEGER DEFAULT 0,
            game_stage TEXT DEFAULT 'Chrysalis'
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS medications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            medication_name TEXT NOT NULL,
            scheduled_time TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS medication_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            medication_name TEXT NOT NULL,
            scheduled_time TEXT NOT NULL,
            taken_time TEXT,
            status TEXT NOT NULL CHECK(status IN ('taken', 'late', 'missed')),
            butterfly_bucks_earned INTEGER DEFAULT 0,
            log_date TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    conn.commit()
    conn.close()


def seed_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] > 0:
        conn.close()
        return

    patients = [
        ("taylor", "pass123", "Taylor Smith", "taylor@email.com", "patient", 120, "Caterpillar"),
        ("maya",   "pass123", "Maya Johnson", "maya@email.com",   "patient", 45,  "Chrysalis"),
        ("alex",   "pass123", "Alex Rivera",  "alex@email.com",   "patient", 200, "Butterfly"),
        ("jordan", "pass123", "Jordan Lee",   "jordan@email.com", "patient", 80,  "Caterpillar"),
    ]
    for p in patients:
        cursor.execute("""
            INSERT OR IGNORE INTO users (username, password, full_name, email, role, butterfly_bucks, game_stage)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, p)

    cursor.execute("""
        INSERT OR IGNORE INTO users (username, password, full_name, email, role)
        VALUES ('drEmma', 'clinic123', 'Dr. Emma Davis', 'dr.emma@clinic.com', 'clinician')
    """)
    conn.commit()

    cursor.execute("SELECT id FROM users WHERE role = 'patient'")
    patient_ids = [r["id"] for r in cursor.fetchall()]

    medications_list = ["Hydroxychloroquine", "Prednisone", "Methotrexate"]
    statuses_pool = [
        ["taken","taken","late","taken","missed","taken","taken"],
        ["missed","taken","taken","taken","late","missed","taken"],
        ["taken","late","taken","taken","taken","taken","missed"],
        ["taken","taken","taken","missed","taken","late","taken"],
    ]

    from datetime import timedelta
    today = datetime.now()

    for i, uid in enumerate(patient_ids):
        for med in medications_list:
            cursor.execute("INSERT INTO medications (user_id, medication_name, scheduled_time) VALUES (?,?,?)",
                           (uid, med, "11:00 AM"))
        for day_offset in range(6, -1, -1):
            log_date = (today - timedelta(days=day_offset)).strftime("%Y-%m-%d")
            status = statuses_pool[i][6 - day_offset]
            bb = 2 if status == "taken" else 1 if status == "late" else 0
            taken_time = f"{log_date} 11:05:00" if status == "taken" else f"{log_date} 13:30:00" if status == "late" else None
            cursor.execute("""
                INSERT INTO medication_logs
                (user_id, medication_name, scheduled_time, taken_time, status, butterfly_bucks_earned, log_date)
                VALUES (?,?,?,?,?,?,?)
            """, (uid, "Hydroxychloroquine", "11:00 AM", taken_time, status, bb, log_date))

    conn.commit()
    conn.close()
    print("✅ Sample data seeded!")


# ── AUTH ──

@app.route("/")
def home():
    return jsonify({"message": "Lupus Butterfly Backend ✅"})


@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    full_name = data.get("full_name")
    email     = data.get("email")
    username  = data.get("username")
    password  = data.get("password")

    if not all([full_name, email, username, password]):
        return jsonify({"error": "All fields are required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO users (username, password, full_name, email, role, butterfly_bucks, game_stage)
            VALUES (?, ?, ?, ?, 'patient', 0, 'Chrysalis')
        """, (username, password, full_name, email))
        user_id = cursor.lastrowid
        for med in ["Hydroxychloroquine", "Prednisone"]:
            cursor.execute("INSERT INTO medications (user_id, medication_name, scheduled_time) VALUES (?,?,?)",
                           (user_id, med, "11:00 AM"))
        conn.commit()
        conn.close()
        return jsonify({"message": "Account created successfully!"}), 201
    except sqlite3.IntegrityError:
        conn.close()
        return jsonify({"error": "Username already exists"}), 409


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    if not user:
        return jsonify({"error": "Invalid credentials"}), 401
    return jsonify({
        "user_id": user["id"], "full_name": user["full_name"],
        "email": user["email"], "role": user["role"],
        "butterfly_bucks": user["butterfly_bucks"], "game_stage": user["game_stage"]
    }), 200


# ── PATIENT ──

@app.route("/patient/<int:user_id>/dashboard")
def patient_dashboard(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
    user = cursor.fetchone()
    if not user:
        conn.close()
        return jsonify({"error": "Not found"}), 404
    today = datetime.now().strftime("%Y-%m-%d")
    cursor.execute("SELECT * FROM medication_logs WHERE user_id=? AND log_date=?", (user_id, today))
    today_logs = cursor.fetchall()
    cursor.execute("SELECT * FROM medications WHERE user_id=?", (user_id,))
    scheduled = cursor.fetchall()
    conn.close()
    return jsonify({
        "full_name": user["full_name"],
        "butterfly_bucks": user["butterfly_bucks"],
        "game_stage": user["game_stage"],
        "scheduled_medications": [{"name": m["medication_name"], "time": m["scheduled_time"]} for m in scheduled],
        "today_logs": [{"medication": l["medication_name"], "status": l["status"], "taken_time": l["taken_time"]} for l in today_logs]
    }), 200


@app.route("/patient/<int:user_id>/history")
def patient_history(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM medication_logs WHERE user_id=?
        ORDER BY log_date DESC, taken_time DESC LIMIT 30
    """, (user_id,))
    rows = cursor.fetchall()
    conn.close()
    return jsonify([{
        "id": r["id"], "medication_name": r["medication_name"],
        "scheduled_time": r["scheduled_time"], "taken_time": r["taken_time"],
        "status": r["status"], "butterfly_bucks_earned": r["butterfly_bucks_earned"],
        "log_date": r["log_date"]
    } for r in rows]), 200


@app.route("/log_medication", methods=["POST"])
def log_medication():
    data = request.get_json()
    user_id = data.get("user_id")
    medication_name = data.get("medication_name")
    status = data.get("status")
    scheduled_time = data.get("scheduled_time", "11:00 AM")
    if not all([user_id, medication_name, status]):
        return jsonify({"error": "Missing fields"}), 400
    taken_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_date   = datetime.now().strftime("%Y-%m-%d")
    bb = 2 if status == "taken" else 1 if status == "late" else 0
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO medication_logs
        (user_id, medication_name, scheduled_time, taken_time, status, butterfly_bucks_earned, log_date)
        VALUES (?,?,?,?,?,?,?)
    """, (user_id, medication_name, scheduled_time, taken_time, status, bb, log_date))
    cursor.execute("UPDATE users SET butterfly_bucks=butterfly_bucks+? WHERE id=?", (bb, user_id))
    cursor.execute("SELECT butterfly_bucks FROM users WHERE id=?", (user_id,))
    total_bb = cursor.fetchone()["butterfly_bucks"]
    stage = "Butterfly" if total_bb >= 150 else "Caterpillar" if total_bb >= 50 else "Chrysalis"
    cursor.execute("UPDATE users SET game_stage=? WHERE id=?", (stage, user_id))
    conn.commit()
    conn.close()
    return jsonify({
        "message": "✅ Your data has been saved to the backend database!",
        "butterfly_bucks_earned": bb,
        "new_stage": stage
    }), 201


# ── CLINICIAN ──

@app.route("/clinician/patients")
def get_patients():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE role='patient'")
    patients = cursor.fetchall()
    conn.close()
    return jsonify([{"id": p["id"], "full_name": p["full_name"], "username": p["username"],
                     "butterfly_bucks": p["butterfly_bucks"], "game_stage": p["game_stage"]} for p in patients]), 200


@app.route("/clinician/alerts")
def get_alerts():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT ml.*, u.full_name FROM medication_logs ml
        JOIN users u ON ml.user_id=u.id
        WHERE ml.status='missed' ORDER BY ml.log_date DESC LIMIT 20
    """)
    alerts = cursor.fetchall()
    conn.close()
    return jsonify([{"patient_name": a["full_name"], "medication_name": a["medication_name"],
                     "log_date": a["log_date"], "scheduled_time": a["scheduled_time"]} for a in alerts]), 200


@app.route("/clinician/patient/<int:user_id>/adherence")
def patient_adherence(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT log_date, status, COUNT(*) as count FROM medication_logs
        WHERE user_id=? GROUP BY log_date, status ORDER BY log_date DESC LIMIT 30
    """, (user_id,))
    rows = cursor.fetchall()
    conn.close()
    return jsonify([{"log_date": r["log_date"], "status": r["status"], "count": r["count"]} for r in rows]), 200


if __name__ == "__main__":
    create_tables()
    seed_data()
    app.run(debug=True)