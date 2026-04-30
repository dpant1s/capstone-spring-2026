# 🦋 Lupus Butterfly — Medication Adherence App
**Team Monarch | Capstone I | Spring 2026**

---

## Project Overview
Lupus Butterfly is a medication adherence application designed for Lupus patients. The app addresses the challenge of medication non-compliance by combining real-time tracking with a gamified reward system (Butterfly Bucks) to motivate consistent medication intake. Clinicians can monitor patient adherence through a dedicated dashboard with real-time alerts.

---

## Project Status
✅ **MVP Prototype Complete** — Sprints 0–3 finalized. Full mobile development continues in Capstone II.

---

## Team Information
**Team Name:** Team Monarch

| Name | Role |
|------|------|
| Jinh Nguyen | Team Lead, MVP UI Screenshots, Project Management Review, Mobile HTML Prototype, PowerPoint |
| Dikshya Pant | Backend Development, Streamlit Web Prototype, MVP Live Demo |
| Aniya Taylor | UI/UX Design, Wireframes, Plans for Future Sprints 4 & 5 |
| Remonda Ayad | Reflections & Lessons Learned, Documentation |
| Movika Tamang | Updated Documents Sprints 0–3 (Requirements, Design Diagrams, ERDs, Testing Template) |

**Course Staff:**
- Instructor: Diana Rabah
- Teaching Assistant: Sai Sri Harsha Chakravarthula

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python / Flask |
| Database | SQLite |
| Web Prototype | Streamlit (UI.py) |
| Mobile Prototype | HTML / CSS / JavaScript |
| Version Control | GitHub |
| Project Management | Trello (Kanban) |

---

## How to Run the Web Prototype

### Prerequisites
```bash
pip3 install flask streamlit requests
```

### Step 1 — Start the Flask backend (Terminal 1)
```bash
git clone https://github.com/dpant1s/capstone-spring-2026.git
cd capstone-spring-2026
python3 app.py
```
Backend runs at: `http://127.0.0.1:5000`

### Step 2 — Start the Streamlit frontend (Terminal 2)
```bash
streamlit run UI.py
```
Open browser at: `http://localhost:8501`

### Demo Accounts
| Role | Username | Password |
|------|----------|----------|
| Patient | taylor | pass123 |
| Patient | maya | pass123 |
| Clinician | drEmma | clinic123 |

---

## Features (MVP)

### Patient
- ✅ Sign up & login
- ✅ View medication status (taken, late, missed)
- ✅ Mark medications as taken — live database update
- ✅ Earn Butterfly Bucks (On-time +2 BB, Late +1 BB, Missed +0 BB)
- ✅ Progress through game stages: Chrysalis 🥚 → Caterpillar 🐛 → Butterfly 🦋
- ✅ View full adherence history

### Clinician
- ✅ Login to dedicated dashboard
- ✅ View non-adherence alerts for patients
- ✅ Search and filter patient list
- ✅ View individual patient adherence charts

---

## Butterfly Bucks Reward System
| Action | Reward |
|--------|--------|
| Medication taken on time | +2 BB |
| Medication taken late | +1 BB |
| Medication missed | 0 BB |

**Game Stages:**
- 🥚 Chrysalis: 0–49 BB
- 🐛 Caterpillar: 50–149 BB
- 🦋 Butterfly: 150+ BB

---

## MVP Feature Scope

### Included in MVP
- Flask backend with full medication tracking API
- SQLite database with user, medication, and log schema
- Streamlit web prototype with real working backend
- HTML/CSS mobile prototype (patient app)
- UI wireframes for all primary screens
- Full user flow documentation

### Planned for Capstone II
- Full Android/iOS mobile app
- Bluetooth bottle cap hardware integration
- Live push notifications
- Full authentication system with encryption
- Cloud deployment (Supabase + Streamlit Cloud)

---

## UI Design / Wireframes
UI mockups are located in the `/designs` folder:
- Sign Up Screen
- Patient Home Screen
- Patient Account Page
- Clinician Home Dashboard
- Clinician Account Page

---

## Patient User Flow
1. User creates account or logs in
2. Home dashboard displays medication status, BB balance, and game stage
3. User marks medication as taken → app logs timestamp
4. Butterfly Bucks awarded based on adherence timing
5. User progresses through game stages by accumulating BB
6. User views adherence history and Butterfly Bank

## Clinician User Flow
1. Clinician logs into dedicated dashboard
2. Views non-adherence alerts for patients who missed medications
3. Searches patient list and views individual adherence data
4. Monitors weekly/monthly adherence trends via charts
