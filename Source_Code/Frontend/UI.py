import streamlit as st
import requests
from datetime import datetime

API = "http://127.0.0.1:5000"

st.set_page_config(page_title="Lupus Butterfly", page_icon="🦋", layout="centered")

# ── Pure CSS dreamy background ──
bg_style = """
    radial-gradient(ellipse at 25% 25%, rgba(255,150,200,0.4) 0%, transparent 50%),
    radial-gradient(ellipse at 75% 15%, rgba(230,130,255,0.35) 0%, transparent 45%),
    radial-gradient(ellipse at 80% 75%, rgba(255,160,210,0.3) 0%, transparent 40%),
    radial-gradient(ellipse at 20% 80%, rgba(180,100,255,0.3) 0%, transparent 45%),
    linear-gradient(145deg, #5b0fa0 0%, #8b20c8 30%, #a855f7 55%, #7c3aed 80%, #4a0080 100%)
"""

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Nunito:wght@300;400;600;700;800&display=swap');

*, *::before, *::after {{{{ box-sizing: border-box; }}}}

.stApp {{{{
    background: 
        linear-gradient(180deg, rgba(255,220,235,0.35) 0%, rgba(220,180,255,0.35) 50%, rgba(180,200,255,0.35) 100%),
        {bg_style};
    min-height: 100vh;
    font-family: 'Nunito', sans-serif;
}}}}
#MainMenu, footer, header {{ visibility: hidden; }}

/* ── FLOATING BUTTERFLIES ── */
.butterfly {{
    position: fixed;
    font-size: 28px;
    opacity: 0.35;
    animation: float linear infinite;
    pointer-events: none;
    z-index: 0;
    filter: drop-shadow(0 0 8px rgba(180,100,220,0.4));
}}
.b1 {{ left: 8%;  animation-duration: 14s; animation-delay: 0s;   top: 15%; }}
.b2 {{ left: 78%; animation-duration: 18s; animation-delay: -5s;  top: 35%; }}
.b3 {{ left: 45%; animation-duration: 22s; animation-delay: -10s; top: 60%; }}

@keyframes float {{
    0%   {{ transform: translateY(0px)   rotate(-8deg) scale(1);   opacity: 0.25; }}
    25%  {{ transform: translateY(-30px) rotate(8deg)  scale(1.1); opacity: 0.4;  }}
    50%  {{ transform: translateY(-15px) rotate(-5deg) scale(0.95);opacity: 0.35; }}
    75%  {{ transform: translateY(-40px) rotate(10deg) scale(1.05);opacity: 0.45; }}
    100% {{ transform: translateY(0px)   rotate(-8deg) scale(1);   opacity: 0.25; }}
}}
.block-container {{ padding-top: 0.5rem !important; padding-bottom: 2rem !important; max-width: 460px !important; }}

/* ── NUCLEAR BACKGROUND OVERRIDE ── */
html, body, [data-testid="stAppViewContainer"],
[data-testid="stAppViewContainer"] > .main,
[data-testid="stAppViewBlockContainer"],
.main, .main > div, section.main,
section.main > div, .main .block-container,
[data-testid="stHeader"], [data-testid="stToolbar"],
div[class*="appview"], div[class*="main"] {{
    background: transparent !important;
    background-color: transparent !important;
}}

body {{
    background: linear-gradient(135deg, #e891d4 0%, #c87ae0 25%, #b56ee8 50%, #d47ee0 75%, #e888cc 100%) !important;
    background-attachment: fixed !important;
}}

/* ── CARDS ── */
.card {{
    background: rgba(255,255,255,0.75);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255,255,255,0.6);
    border-radius: 24px;
    padding: 24px 22px;
    margin: 10px 0;
    box-shadow: 0 8px 32px rgba(120,40,180,0.12);
}}
.card p {{ color: #3b0764 !important; }}
.card b {{ color: #3b0764 !important; }}
.card-white {{
    background: rgba(255,255,255,0.92);
    border-radius: 20px;
    padding: 18px 20px;
    margin: 8px 0;
    box-shadow: 0 4px 16px rgba(120,0,180,0.15);
    color: #3b0764 !important;
}}
.card-white p, .card-white span, .card-white b {{
    color: #3b0764 !important;
    -webkit-text-fill-color: #3b0764 !important;
}}

/* ── INPUTS ── */
.stTextInput label, .stCheckbox label {{
    color: #3b0764 !important;
    font-family: 'Nunito', sans-serif !important;
    font-size: 12px !important;
    font-weight: 700 !important;
    letter-spacing: 1.2px !important;
    text-transform: uppercase !important;
}}
.stTextInput input {{
    background: rgba(10,0,30,0.7) !important;
    border: 1.5px solid rgba(255,255,255,0.35) !important;
    border-radius: 14px !important;
    color: white !important;
    -webkit-text-fill-color: white !important;
    font-family: 'Nunito', sans-serif !important;
    font-size: 15px !important;
    padding: 12px 16px !important;
    caret-color: white !important;
}}
.stTextInput input::placeholder {{ color: rgba(255,255,255,0.35) !important; -webkit-text-fill-color: rgba(255,255,255,0.35) !important; }}
.stTextInput input:focus {{ border-color: #e879f9 !important; box-shadow: 0 0 0 3px rgba(232,121,249,0.3) !important; background: rgba(10,0,30,0.85) !important; }}
.stTextInput input:-webkit-autofill,
.stTextInput input:-webkit-autofill:focus {{
    -webkit-box-shadow: 0 0 0 1000px rgba(10,0,30,0.9) inset !important;
    -webkit-text-fill-color: white !important;
}}

/* ── BUTTONS ── */
.stButton > button {{
    background: linear-gradient(135deg, #7c3aed 0%, #a855f7 50%, #c084fc 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 50px !important;
    padding: 14px 32px !important;
    font-family: 'Nunito', sans-serif !important;
    font-size: 16px !important;
    font-weight: 800 !important;
    width: 100% !important;
    letter-spacing: 0.5px !important;
    box-shadow: 0 6px 24px rgba(124,58,237,0.55) !important;
    transition: all 0.2s !important;
}}
.stButton > button:hover {{
    background: linear-gradient(135deg, #6d28d9 0%, #9333ea 100%) !important;
    box-shadow: 0 8px 30px rgba(124,58,237,0.75) !important;
    transform: translateY(-2px) !important;
}}

/* ── METRICS ── */
[data-testid="stMetric"] {{
    background: rgba(255,255,255,0.7) !important;
    border: 1px solid rgba(124,58,237,0.2) !important;
    border-radius: 16px !important;
    padding: 12px 8px !important;
    text-align: center !important;
}}
[data-testid="stMetricLabel"] p {{ color: #7c3aed !important; font-size: 11px !important; font-weight: 700 !important; text-transform: uppercase !important; letter-spacing: 1px !important; }}
[data-testid="stMetricValue"] {{ color: #3b0764 !important; font-size: 20px !important; font-weight: 800 !important; }}

/* ── PROGRESS ── */
.stProgress > div > div {{ background: linear-gradient(90deg, #7c3aed, #e879f9) !important; border-radius: 10px !important; height: 12px !important; }}
.stProgress > div {{ background: rgba(255,255,255,0.2) !important; border-radius: 10px !important; height: 12px !important; }}

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {{ background: linear-gradient(180deg, #6b1a7a 0%, #9b2fa8 40%, #c44fb5 100%) !important; border-right: 1px solid rgba(255,180,230,0.3) !important; }}
[data-testid="stSidebar"] .stButton > button {{ background: rgba(255,255,255,0.07) !important; border: 1px solid rgba(255,255,255,0.12) !important; box-shadow: none !important; font-size: 14px !important; border-radius: 12px !important; margin-bottom: 6px !important; text-align: left !important; }}
[data-testid="stSidebar"] .stButton > button:hover {{ background: rgba(192,132,252,0.2) !important; border-color: #c084fc !important; transform: none !important; }}

/* ── MISC ── */
hr {{ border-color: rgba(124,58,237,0.2) !important; margin: 14px 0 !important; }}
h1,h2,h3,h4 {{ font-family: 'Playfair Display', serif !important; color: #3b0764 !important; }}
.stMarkdown p {{ color: #3b0764 !important; font-family: 'Nunito', sans-serif !important; }}
.stAlert {{ border-radius: 14px !important; }}
.stToggle label {{ color: #3b0764 !important; font-family: 'Nunito', sans-serif !important; }}

/* ── BADGES ── */
.badge {{ display:inline-block; padding:4px 14px; border-radius:50px; font-size:12px; font-weight:800; letter-spacing:0.5px; font-family:'Nunito',sans-serif; }}
.badge-taken  {{ background:rgba(34,197,94,0.2);  color:#4ade80; border:1px solid rgba(34,197,94,0.45); }}
.badge-late   {{ background:rgba(251,191,36,0.2); color:#fcd34d; border:1px solid rgba(251,191,36,0.45); }}
.badge-missed {{ background:rgba(239,68,68,0.2);  color:#f87171; border:1px solid rgba(239,68,68,0.45); }}

.quick-btn {{
    background: rgba(255,255,255,0.75);
    border: 1px solid rgba(124,58,237,0.2);
    border-radius: 18px;
    padding: 16px 10px;
    text-align: center;
    cursor: pointer;
    transition: all 0.2s;
    box-shadow: 0 4px 12px rgba(124,58,237,0.1);
}}
.quick-btn:hover {{ background: rgba(255,255,255,0.95); transform: translateY(-2px); }}
.quick-btn-icon {{ font-size: 28px; display:block; margin-bottom:6px; }}
.quick-btn-label {{ font-size: 11px; font-weight: 700; color: #7c3aed; font-family:'Nunito',sans-serif; letter-spacing:0.5px; }}

/* ── ALERT CARD ── */
.alert-card {{ background:rgba(239,68,68,0.1); border:1px solid rgba(239,68,68,0.3); border-left:4px solid #ef4444; border-radius:14px; padding:14px 16px; margin:8px 0; }}

/* ── DEMO BOX ── */
.demo-box {{ background:rgba(255,255,255,0.15); border:1px solid rgba(255,255,255,0.35); border-radius:16px; padding:16px 20px; margin-top:16px; font-size:13px; color:white; font-family:'Nunito',sans-serif; font-weight:600; }}
.demo-box code {{ background:rgba(255,255,255,0.25); border-radius:6px; padding:3px 10px; font-size:13px; color:white; font-weight:700; }}

.stage-card {{
    background: linear-gradient(135deg, rgba(255,255,255,0.8), rgba(240,220,255,0.6));
    border: 1px solid rgba(124,58,237,0.2);
    border-radius: 24px;
    padding: 20px;
    text-align: center;
    margin: 10px 0;
}}
.jar-card {{
    background: rgba(255,255,255,0.8);
    border: 1px solid rgba(124,58,237,0.15);
    border-radius: 20px;
    padding: 16px 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin: 10px 0;
    box-shadow: 0 4px 16px rgba(124,58,237,0.1);
}}
</style>
""", unsafe_allow_html=True)


# ── Inject floating butterflies into page ──
st.markdown("""
<div class='butterfly b1'>🦋</div>
<div class='butterfly b2'>🦋</div>
<div class='butterfly b3'>🦋</div>
""", unsafe_allow_html=True)

# ── SESSION STATE ──
for k, v in [("logged_in",False),("user",None),("page","login"),("selected_patient",None),("show_signup",False)]:
    if k not in st.session_state: st.session_state[k] = v

def nav(page): st.session_state.page = page
def stage_emoji(s): return {"Chrysalis":"🥚","Caterpillar":"🐛","Butterfly":"🦋"}.get(s,"🥚")
def stage_progress(bb):
    if bb >= 150: return 100
    elif bb >= 50: return int(((bb-50)/100)*100)
    return int((bb/50)*100)
def badge(s): return f'<span class="badge badge-{s}">{s.upper()}</span>'
def greeting():
    h = datetime.now().hour
    return "Good Morning" if h<12 else "Good Afternoon" if h<17 else "Good Evening"

# ────────────────────────────────────────────
# SIGN UP PAGE
# ────────────────────────────────────────────
def show_signup():
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align:center; margin-bottom:16px;'>
        <span style='font-size:48px; filter:drop-shadow(0 0 20px rgba(232,121,249,0.9));'>🦋</span>
        <p style='font-family:Playfair Display,serif; font-size:28px; font-weight:700; color:white; margin:6px 0 2px;'>Lupus Butterfly</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; font-family:Playfair Display,serif; margin-bottom:20px;'>Create Your Account</h3>", unsafe_allow_html=True)

    full_name = st.text_input("👤  Full Name", placeholder="Taylor Smith", key="su_name")
    email     = st.text_input("✉️  Email Address", placeholder="your@email.com", key="su_email")
    username  = st.text_input("🔑  Username", placeholder="Choose a username", key="su_user")
    password  = st.text_input("🔒  Password", type="password", placeholder="Create a password", key="su_pass")
    confirm   = st.text_input("🔒  Confirm Password", type="password", placeholder="Repeat your password", key="su_conf")
    agree     = st.checkbox("✅  I agree to the Terms & Privacy Policy")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🦋  Create Account"):
        if not all([full_name, email, username, password, confirm]):
            st.warning("Please fill in all fields.")
        elif password != confirm:
            st.error("❌ Passwords do not match.")
        elif not agree:
            st.warning("Please agree to the Terms & Privacy Policy.")
        else:
            try:
                res = requests.post(f"{API}/signup", json={
                    "full_name": full_name, "email": email,
                    "username": username, "password": password
                })
                if res.status_code == 201:
                    st.success("✅ Account created! Please log in.")
                    st.session_state.show_signup = False
                    st.rerun()
                elif res.status_code == 409:
                    st.error("❌ Username already taken. Try another.")
                else:
                    st.error("Something went wrong. Try again.")
            except:
                st.error("⚠️ Cannot connect to backend.")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='text-align:center; margin-top:16px;'>", unsafe_allow_html=True)
    if st.button("Already have an account? Log In"):
        st.session_state.show_signup = False
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)


# ────────────────────────────────────────────
# LOGIN PAGE
# ────────────────────────────────────────────
def show_login():
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align:center; margin-bottom:16px;'>
        <span style='font-size:56px; filter:drop-shadow(0 0 24px rgba(232,121,249,1));'>🦋</span>
        <p style='font-family:Playfair Display,serif; font-size:30px; font-weight:700; color:white; margin:6px 0 2px;'>Lupus Butterfly</p>
        <p style='color:#f0abfc; font-size:13px; letter-spacing:2px; text-transform:uppercase; margin:0;'>Medication Adherence App</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; font-family:Playfair Display,serif; margin-bottom:20px;'>Welcome Back 💜</h3>", unsafe_allow_html=True)

    username = st.text_input("Username", placeholder="Enter your username", key="li_user")
    password = st.text_input("Password", type="password", placeholder="Enter your password", key="li_pass")
    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Login"):
        if username and password:
            try:
                res = requests.post(f"{API}/login", json={"username": username, "password": password}, timeout=5)
                if res.status_code == 200:
                    user = res.json()
                    st.session_state.logged_in = True
                    st.session_state.user = user
                    st.session_state.page = "patient_home" if user["role"] == "patient" else "clinician_home"
                    st.rerun()
                else:
                    st.error("❌ Invalid username or password.")
            except requests.exceptions.ConnectionError:
                st.error("⚠️ Cannot connect to backend. Make sure Flask is running.")
            except requests.exceptions.Timeout:
                st.error("⚠️ Request timed out. Make sure Flask is running.")
            except Exception as e:
                st.error(f"⚠️ Unexpected error: {e}")
        else:
            st.warning("Please fill in both fields.")
    st.markdown("</div>", unsafe_allow_html=True)

    # Sign up link
    st.markdown("<div style='text-align:center; margin-top:12px;'>", unsafe_allow_html=True)
    if st.button("Don't have an account? Sign Up"):
        st.session_state.show_signup = True
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='demo-box'>
        <b>🔑 Demo Accounts</b><br><br>
        👤 Patient: &nbsp;<code>taylor</code> / <code>pass123</code><br>
        👤 Patient: &nbsp;<code>maya</code> / <code>pass123</code><br>
        🏥 Clinician: <code>drEmma</code> / <code>clinic123</code>
    </div>""", unsafe_allow_html=True)


# ────────────────────────────────────────────
# PATIENT HOME
# ────────────────────────────────────────────
def show_patient_home():
    user = st.session_state.user
    try:
        response = requests.get(f"{API}/patient/{user['user_id']}/dashboard", timeout=5)
        data = response.json()
    except requests.exceptions.ConnectionError:
        st.error("⚠️ Cannot connect to backend. Make sure Flask is running.")
        return
    except Exception as e:
        st.error(f"⚠️ Error loading dashboard: {e}")
        return

    name  = data["full_name"].split()[0]
    stage = data["game_stage"]
    bb    = data["butterfly_bucks"]
    prog  = stage_progress(bb)

    # Header
    st.markdown(f"""
    <div style='text-align:center; padding:12px 0 8px;'>
        <span style='font-size:42px; filter:drop-shadow(0 0 18px rgba(124,58,237,0.5));'>🦋</span>
        <p style='font-family:Playfair Display,serif; font-size:26px; font-weight:700; color:#3b0764; margin:6px 0 2px;'>{greeting()}, {name}!</p>
        <p style='color:#6b21a8; font-size:13px; margin:0;'>{datetime.now().strftime("%A, %B %d, %Y")}</p>
    </div>
    """, unsafe_allow_html=True)

    # Medication status card
    today_logs = data.get("today_logs", [])
    taken_today = sum(1 for l in today_logs if l["status"] == "taken")
    total_meds  = len(data.get("scheduled_medications", []))

    status_text = f"✅ {taken_today} of {total_meds} taken today" if taken_today > 0 else "⏳ No doses logged yet today"
    status_color = "#16a34a" if taken_today > 0 else "#9333ea"
    st.markdown(f"""
    <div class='card-white'>
        <p style='color:#7c3aed; font-weight:800; font-size:14px; margin:0 0 8px; font-family:Nunito,sans-serif;'>💊 Medication Status</p>
        <p style='color:#4b5563; font-size:13px; margin:0; font-family:Nunito,sans-serif;'>Scheduled Dose: <b style="color:#3b0764;">11:00 AM</b></p>
        <p style='color:{status_color}; font-size:14px; font-weight:700; margin:6px 0 0; font-family:Nunito,sans-serif;'>{status_text}</p>
    </div>
    """, unsafe_allow_html=True)

    # Butterfly Bucks jar card
    st.markdown(f"""
    <div class='jar-card'>
        <div>
            <p style='color:#3b0764; font-weight:800; font-size:15px; margin:0 0 4px; font-family:Nunito,sans-serif;'>🫙 Butterfly Bucks</p>
            <p style='color:#6b21a8; font-size:12px; margin:0 0 6px; font-family:Nunito,sans-serif;'>Current Balance</p>
            <p style='color:#7c3aed; font-size:28px; font-weight:800; margin:0; font-family:Nunito,sans-serif;'>{bb} <span style='font-size:14px;'>BB</span></p>
        </div>
        <div style='font-size:52px; filter:drop-shadow(0 0 12px rgba(124,58,237,0.4));'>🫙</div>
    </div>
    """, unsafe_allow_html=True)

    # Stage card with progress
    stage_art = {"Chrysalis": "🥚", "Caterpillar": "🐛", "Butterfly": "🦋"}
    stage_desc = {"Chrysalis": "Just getting started!", "Caterpillar": "Growing stronger!", "Butterfly": "You're thriving!"}
    st.markdown(f"""
    <div class='stage-card'>
        <p style='font-family:Playfair Display,serif; font-size:20px; font-weight:700; color:#3b0764; margin:0 0 4px;'>{stage} Stage</p>
        <p style='color:#6b21a8; font-size:13px; margin:0 0 12px; font-family:Nunito,sans-serif;'>{stage_desc.get(stage,"")}</p>
        <div style='font-size:64px; margin:8px 0; filter:drop-shadow(0 0 20px rgba(124,58,237,0.4));'>{stage_art.get(stage,"🐛")}</div>
    </div>
    """, unsafe_allow_html=True)
    st.progress(prog / 100)
    st.markdown(f"<p style='text-align:center; color:rgba(255,255,255,0.65); font-size:13px; margin-top:4px; font-family:Nunito,sans-serif;'>{prog}% to {'Butterfly 🦋' if stage=='Caterpillar' else 'Caterpillar 🐛' if stage=='Chrysalis' else 'Max Level! 🎉'}</p>", unsafe_allow_html=True)

    # Quick action buttons - display only, navigation via sidebar
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""<div class='quick-btn' onclick="">
            <span class='quick-btn-icon'>💰</span>
            <span class='quick-btn-label'>Butterfly Bank</span>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class='quick-btn'>
            <span class='quick-btn-icon'>🕐</span>
            <span class='quick-btn-label'>Adherence History</span>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""<div class='quick-btn'>
            <span class='quick-btn-icon'>🦋</span>
            <span class='quick-btn-label'>Customise Butterfly</span>
        </div>""", unsafe_allow_html=True)
    st.caption("💡 Use the sidebar to navigate between pages")

    st.markdown("---")

    # Today's medications
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight:800; font-size:16px; margin-bottom:14px;'>💊 Today's Medications</p>", unsafe_allow_html=True)

    if st.session_state.get("last_log_msg"):
        st.success(st.session_state.pop("last_log_msg"))

    if data["scheduled_medications"]:
        for med in data["scheduled_medications"]:
            logged = next((l for l in today_logs if l["medication"] == med["name"]), None)
            col1, col2 = st.columns([3, 2])
            with col1:
                st.markdown(f"<p style='margin:0; font-weight:700; font-size:14px;'>{med['name']}</p><p style='margin:0; color:rgba(255,255,255,0.5); font-size:12px;'>⏰ {med['time']}</p>", unsafe_allow_html=True)
            with col2:
                if logged:
                    st.markdown(badge(logged["status"]), unsafe_allow_html=True)
                else:
                    if st.button("✓ Take", key=f"take_{med['name']}"):
                        try:
                            now = datetime.now()
                            try:
                                sched = datetime.strptime(med["time"], "%I:%M %p").replace(
                                    year=now.year, month=now.month, day=now.day)
                                minutes_late = (now - sched).total_seconds() / 60
                                status = "taken" if minutes_late <= 50 else "late"
                            except:
                                status = "taken"
                            r = requests.post(f"{API}/log_medication", json={
                                "user_id": user["user_id"], "medication_name": med["name"],
                                "status": status, "scheduled_time": med["time"]
                            })
                            if r.status_code == 201:
                                bb_earned = r.json()['butterfly_bucks_earned']
                                st.session_state["last_log_msg"] = f"+{bb_earned} BB 💾 Saved to database."
                                st.rerun()
                        except Exception as e:
                            st.error(f"Could not log: {e}")
            st.markdown("<hr style='margin:10px 0; border-color:rgba(255,255,255,0.1);'>", unsafe_allow_html=True)
    else:
        st.info("No medications scheduled.")

    st.markdown("""<div style='background:rgba(124,58,237,0.2); border-radius:12px; padding:10px 14px; font-size:13px; margin-top:4px; font-family:Nunito,sans-serif;'>
        🟢 On-time <b>+2 BB</b> &nbsp;|&nbsp; 🟡 Late <b>+1 BB</b> &nbsp;|&nbsp; 🔴 Missed <b>+0 BB</b>
    </div>""", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# ────────────────────────────────────────────
# PATIENT HISTORY
# ────────────────────────────────────────────
def show_patient_history():
    user = st.session_state.user
    st.markdown("<p style='font-family:Playfair Display,serif; font-size:24px; font-weight:700;'>📋 Adherence History</p>", unsafe_allow_html=True)
    try: history = requests.get(f"{API}/patient/{user['user_id']}/history").json()
    except: st.error("Cannot connect."); return
    if not history: st.info("No history yet."); return

    total  = len(history)
    taken  = sum(1 for h in history if h["status"]=="taken")
    late   = sum(1 for h in history if h["status"]=="late")
    missed = sum(1 for h in history if h["status"]=="missed")
    rate   = int((taken/total)*100) if total else 0

    col1,col2,col3,col4 = st.columns(4)
    col1.metric("Total",total); col2.metric("✅",taken); col3.metric("🟡",late); col4.metric("🔴",missed)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-weight:700;'>Overall Adherence: <span style='color:#f0abfc; font-size:20px;'>{rate}%</span></p>", unsafe_allow_html=True)
    st.progress(rate/100)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    for h in history:
        col1,col2,col3 = st.columns([3,2,1])
        with col1: st.markdown(f"<p style='margin:0; font-weight:700; font-size:14px;'>{h['medication_name']}</p><p style='margin:0; color:rgba(255,255,255,0.5); font-size:11px;'>{h['log_date']}</p>", unsafe_allow_html=True)
        with col2: st.markdown(badge(h["status"]), unsafe_allow_html=True)
        with col3: st.markdown(f"<p style='color:#f0abfc; font-weight:800; text-align:right; margin:0;'>+{h['butterfly_bucks_earned']} BB</p>", unsafe_allow_html=True)
        st.markdown("<hr style='margin:8px 0; border-color:rgba(255,255,255,0.1);'>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# ────────────────────────────────────────────
# PATIENT ACCOUNT
# ────────────────────────────────────────────
def show_patient_account():
    user = st.session_state.user
    st.markdown("<p style='font-family:Playfair Display,serif; font-size:24px; font-weight:700;'>👤 My Account</p>", unsafe_allow_html=True)

    st.markdown(f"""<div class='card' style='text-align:center;'>
        <div style='font-size:64px; margin-bottom:8px; filter:drop-shadow(0 0 16px rgba(240,171,252,0.7));'>🦋</div>
        <p style='font-family:Playfair Display,serif; font-size:22px; font-weight:700; margin:0;'>{user['full_name']}</p>
        <p style='color:#f0abfc; font-size:13px; margin:4px 0 16px;'>Lupus Patient</p>
        <div style='display:flex; justify-content:center; gap:32px;'>
            <div><p style='font-size:24px; font-weight:800; margin:0; color:#f0abfc;'>{user['butterfly_bucks']}</p><p style='font-size:11px; color:rgba(255,255,255,0.5); margin:0; font-family:Nunito,sans-serif;'>Butterfly Bucks</p></div>
            <div><p style='font-size:24px; margin:0;'>{stage_emoji(user['game_stage'])}</p><p style='font-size:11px; color:rgba(255,255,255,0.5); margin:0; font-family:Nunito,sans-serif;'>{user['game_stage']}</p></div>
        </div>
    </div>""", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight:800; margin-bottom:12px;'>Account Information</p>", unsafe_allow_html=True)
    st.text_input("Full Name", value=user["full_name"], key="acc_name")
    st.text_input("Email Address", value=user.get("email","lupus.patient@email.com"), key="acc_email")
    st.text_input("Phone Number", value="(555) 123-4567", key="acc_phone")
    if st.button("💾  Save Changes"): st.success("Changes saved!")
    if st.button("🗑️  Delete Account"): st.warning("Please contact support to delete your account.")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight:800; margin-bottom:12px;'>🔔 Notification Settings</p>", unsafe_allow_html=True)
    st.toggle("Daily medication reminders", value=True)
    st.toggle("Weekly adherence summary", value=True)
    st.toggle("Clinician updates", value=False)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight:800; margin-bottom:12px;'>🔒 Privacy & Security</p>", unsafe_allow_html=True)
    if st.button("🔑  Change Password"): st.info("Password reset link sent to your email!")
    if st.button("❓  Help & Support"): st.info("Contact: support@lupusbutterfly.app")
    st.markdown("</div>", unsafe_allow_html=True)


# ────────────────────────────────────────────
# CLINICIAN HOME
# ────────────────────────────────────────────
def show_clinician_home():
    user = st.session_state.user
    try:
        patients = requests.get(f"{API}/clinician/patients").json()
        alerts   = requests.get(f"{API}/clinician/alerts").json()
    except: st.error("Cannot connect."); return

    last = user["full_name"].split()[-1]
    st.markdown(f"""<div style='text-align:center; padding:12px 0 8px;'>
        <span style='font-size:42px;'>🏥</span>
        <p style='font-family:Playfair Display,serif; font-size:26px; font-weight:700; color:white; margin:6px 0 2px;'>{greeting()}, Dr. {last}!</p>
        <p style='color:rgba(255,255,255,0.55); font-size:13px; margin:0;'>{datetime.now().strftime("%A, %B %d, %Y")}</p>
    </div>""", unsafe_allow_html=True)

    col1,col2,col3 = st.columns(3)
    col1.metric("👥 Patients", len(patients))
    col2.metric("🚨 Alerts", len(alerts))
    col3.metric("🦋 Butterflies", sum(1 for p in patients if p["game_stage"]=="Butterfly"))

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight:800; font-size:16px; margin-bottom:12px;'>🚨 Non-Adherence Alerts</p>", unsafe_allow_html=True)
    if alerts:
        for a in alerts[:5]:
            st.markdown(f"""<div class='alert-card'>
                <p style='margin:0; font-weight:700; font-family:Nunito,sans-serif;'>⚠️ {a['patient_name']}</p>
                <p style='margin:4px 0 0; color:rgba(255,255,255,0.7); font-size:13px; font-family:Nunito,sans-serif;'>Missed <b>{a['medication_name']}</b> — {a['log_date']} at {a['scheduled_time']}</p>
            </div>""", unsafe_allow_html=True)
    else:
        st.success("✅ No missed medications today!")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight:800; font-size:16px; margin-bottom:12px;'>👥 Patient Overview</p>", unsafe_allow_html=True)
    search = st.text_input("🔍 Search patients", placeholder="Type patient name...", key="cl_search")
    filtered = [p for p in patients if search.lower() in p["full_name"].lower()] if search else patients
    for p in filtered:
        col1,col2,col3,col4 = st.columns([3,2,2,1])
        with col1: st.markdown(f"<p style='margin:0; font-weight:700;'>{p['full_name']}</p><p style='margin:0; color:rgba(255,255,255,0.5); font-size:11px;'>@{p['username']}</p>", unsafe_allow_html=True)
        with col2: st.markdown(f"<p style='color:#f0abfc; margin:0; font-weight:800;'>💰 {p['butterfly_bucks']} BB</p>", unsafe_allow_html=True)
        with col3: st.markdown(f"<p style='margin:0;'>{stage_emoji(p['game_stage'])} {p['game_stage']}</p>", unsafe_allow_html=True)
        with col4:
            if st.button("→", key=f"v_{p['id']}"):
                st.session_state.selected_patient = p; nav("clinician_patient_detail"); st.rerun()
        st.markdown("<hr style='margin:8px 0; border-color:rgba(255,255,255,0.1);'>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# ────────────────────────────────────────────
# CLINICIAN PATIENT DETAIL
# ────────────────────────────────────────────
def show_clinician_patient_detail():
    patient = st.session_state.get("selected_patient")
    if not patient: nav("clinician_home"); st.rerun(); return
    if st.button("← Back"): nav("clinician_home"); st.rerun()

    st.markdown(f"<p style='font-family:Playfair Display,serif; font-size:22px; font-weight:700;'>📊 {patient['full_name']}</p>", unsafe_allow_html=True)
    col1,col2 = st.columns(2)
    col1.metric("💰 Butterfly Bucks", patient["butterfly_bucks"])
    col2.metric("Stage", f"{stage_emoji(patient['game_stage'])} {patient['game_stage']}")

    try: data = requests.get(f"{API}/clinician/patient/{patient['id']}/adherence").json()
    except: st.error("Cannot connect."); return

    if data:
        import pandas as pd
        df = pd.DataFrame(data)
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<p style='font-weight:800; margin-bottom:12px;'>📅 Adherence Trend</p>", unsafe_allow_html=True)
        pivot = df.pivot_table(index="log_date", columns="status", values="count", fill_value=0)
        st.bar_chart(pivot)
        st.markdown("</div>", unsafe_allow_html=True)


# ────────────────────────────────────────────
# CLINICIAN ACCOUNT
# ────────────────────────────────────────────
def show_clinician_account():
    user = st.session_state.user
    st.markdown("<p style='font-family:Playfair Display,serif; font-size:24px; font-weight:700;'>👤 Clinician Account</p>", unsafe_allow_html=True)
    st.markdown(f"""<div class='card' style='text-align:center;'>
        <div style='font-size:64px; margin-bottom:8px;'>🏥</div>
        <p style='font-family:Playfair Display,serif; font-size:22px; font-weight:700; margin:0;'>{user['full_name']}</p>
        <p style='color:#f0abfc; font-size:13px; margin:4px 0;'>Clinician</p>
    </div>""", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight:800; margin-bottom:12px;'>Account Information</p>", unsafe_allow_html=True)
    st.text_input("Full Name", value=user["full_name"])
    st.text_input("Email", value=user.get("email","dr.emma@clinic.com"))
    if st.button("💾  Save Changes"): st.success("Saved!")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight:800; margin-bottom:12px;'>🔔 Notification Settings</p>", unsafe_allow_html=True)
    st.toggle("Non-adherence alerts", value=True)
    st.toggle("Weekly patient summaries", value=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight:800; margin-bottom:12px;'>👥 Patient Access Management</p>", unsafe_allow_html=True)
    st.info("You have access to all registered patients.")
    if st.button("Manage Access"): st.info("Full access management coming in Capstone II.")
    st.markdown("</div>", unsafe_allow_html=True)


# ────────────────────────────────────────────
# SIDEBAR
# ────────────────────────────────────────────
def show_sidebar():
    user = st.session_state.user
    with st.sidebar:
        st.markdown(f"""<div style='text-align:center; padding:16px 0 8px;'>
            <div style='font-size:38px; filter:drop-shadow(0 0 14px rgba(232,121,249,0.8));'>🦋</div>
            <p style='font-family:Playfair Display,serif; font-size:18px; color:white; margin:4px 0 2px;'>Lupus Butterfly</p>
            <p style='color:#f0abfc; font-size:12px; margin:0;'>{user['full_name']}</p>
            <p style='color:rgba(255,255,255,0.4); font-size:11px; margin:2px 0 16px; font-family:Nunito,sans-serif;'>{user['role'].capitalize()}</p>
        </div>""", unsafe_allow_html=True)
        st.markdown("---")
        if user["role"] == "patient":
            if st.button("🏠  Home"):    nav("patient_home");    st.rerun()
            if st.button("📋  History"): nav("patient_history"); st.rerun()
            if st.button("👤  Account"): nav("patient_account"); st.rerun()
        else:
            if st.button("🏥  Dashboard"): nav("clinician_home");    st.rerun()
            if st.button("👤  Account"):   nav("clinician_account"); st.rerun()
        st.markdown("---")
        if st.button("🚪  Logout"):
            for k,v in [("logged_in",False),("user",None),("page","login"),("selected_patient",None),("show_signup",False)]:
                st.session_state[k] = v
            st.rerun()


# ────────────────────────────────────────────
# ROUTER
# ────────────────────────────────────────────
if not st.session_state.logged_in:
    if st.session_state.show_signup:
        show_signup()
    else:
        show_login()
else:
    show_sidebar()
    page = st.session_state.page
    if   page == "patient_home":             show_patient_home()
    elif page == "patient_history":          show_patient_history()
    elif page == "patient_account":          show_patient_account()
    elif page == "clinician_home":           show_clinician_home()
    elif page == "clinician_patient_detail": show_clinician_patient_detail()
    elif page == "clinician_account":        show_clinician_account()