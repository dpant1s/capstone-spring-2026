# 🦋 The Butterfly Project — Lupus Medication Adherence App
**Team 5 | Team Monarch | Capstone II | Fall 2026**

---

## Project Overview
The Butterfly Project (Lupus Butterfly) is a medication adherence application designed for Lupus patients. The app addresses medication non-compliance by combining real-time tracking with a gamified reward system (Butterfly Bucks) to motivate consistent medication intake. Clinicians can monitor patient adherence through a dedicated dashboard with real-time alerts.

---

## Project Status
**MVP Prototype Complete** (Capstone I) — Full mobile app development, cloud deployment, and authentication in progress for Capstone II.

---

## Team Information
**Team Name:** Team Monarch | **Project Name:** The Butterfly Project | **Team Number:** 5

| Name | Role |
|------|------|
| Jinh Nguyen | Team Lead, Mobile App Architecture |
| Dikshya Pant | Backend Development, Cloud Deployment |
| Aniya Taylor | UI/UX Design, Mobile Screens |
| Remonda Ayad | Testing & QA Documentation |
| Movika Tamang | Documentation, Design Diagrams |

See [CONTRIBUTIONS.md](./CONTRIBUTIONS.md) for a full breakdown of individual work.

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python / Flask |
| Database | SQLite (migrating to Supabase for Capstone II) |
| Web Prototype | Streamlit (UI.py) |
| Mobile App | Android/iOS (in development) |
| Version Control | GitHub |
| Project Management | Trello (Kanban) |

---

## Folder Structure

```
capstone-spring-2026/
├── README.md
├── CONTRIBUTIONS.md
│
├── Source_Code/
│   ├── Backend/
│   │   ├── app.py              # Flask REST API
│   │   ├── database/           # SQLite schema & models
│   │   └── services/           # Business logic (adherence, rewards)
│   │
│   ├── Frontend/
│   │   ├── UI.py                # Streamlit web prototype
│   │   └── mobile/               # HTML/CSS/JS mobile prototype
│
├── Testing/
│   ├── test_cases/
│   └── test_results/
│
└── Documentation/
    ├── SRS/
    ├── design_diagrams/
    └── wireframes/
```

---

## How to Run the Web Prototype

### Prerequisites
```bash
pip3 install flask streamlit requests
```

### Step 1 — Start the Flask backend (Terminal 1)
```bash
git clone https://github.com/dikshyapant/capstone-spring-2026.git
cd capstone-spring-2026/Source_Code/Backend
pip3 install -r requirements.txt
python3 app.py
```
Backend runs at: `http://127.0.0.1:5000`

### Step 2 — Start the Streamlit frontend (Terminal 2)
```bash
cd capstone-spring-2026/Source_Code/Frontend
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

## Features (MVP — Capstone I)

### Patient
- Sign up & login
- View medication status (taken, late, missed)
- Mark medications as taken — live database update
- Earn Butterfly Bucks (On-time +2 BB, Late +1 BB, Missed +0 BB)
- Progress through game stages: Chrysalis 🥚 → Caterpillar 🐛 → Butterfly 🦋
- View full adherence history

### Clinician
- Login to dedicated dashboard
- View non-adherence alerts for patients
- Search and filter patient list
- View individual patient adherence charts

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

## Testing
Test cases and results are tracked in `/Testing`. Backend endpoints are covered by manual test cases in Capstone I; automated test coverage is planned for Capstone II.

---

## Capstone II Roadmap
- Full Android/iOS mobile app
- Bluetooth bottle cap hardware integration
- Live push notifications
- Full authentication system with encryption
- Cloud deployment (Supabase + Streamlit Cloud)

---

## UI Design / Wireframes
UI mockups are located in `Documentation/wireframes`:
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
