# Capstone Project – Team Monarch

## Project Overview
This repository contains the work for Team Monarch’s Capstone Project. The project is currently in the design and early development phase (Sprints 0–3). The focus is on gathering requirements, designing the system, and developing initial prototype functionalities.

---

## Project Status
The team is currently in **Sprint 3**, focusing on refining design artifacts and demonstrating initial working features through a prototype.

---

## Team Information
**Team Name:** Team Monarch  

### Team Members
- Jinh Nguyen (Team Lead)
- Dikshya Pant
- Aniya Taylor
- Movika Tamang
- Remonda Ayad

---

## Course Staff
- Instructor: Diana Rabah  
- Teaching Assistant: Sai Sri Harsha Chakravarthula  

---

## Work Completed (Sprints 0–3)
- GitHub repository setup
- Team organization and communication established
- Trello Kanban board created (managed by team lead)
- Initial requirements gathering
- Design discussions and documentation (SRS, diagrams, etc.)
- Wireframes and system planning
- Initial prototype development (backend setup and basic functionality)

---

## Current Focus (Sprint 3)
- Finalizing design documents
- Refining system requirements
- Developing and improving prototype functionalities
- Preparing deliverables for submission and demonstration

---

## Tools & Technologies
- GitHub – version control and collaboration
- Trello – task and sprint management
- Additional tools and technologies will be finalized as development progresses

---

## Repository Access
This repository is actively used by Team Monarch for project collaboration.  
Team members have been added as contributors.  

Access for course staff (TA and instructor) has been provided / is being maintained.

## How to Run the Backend (MVP)

1. Clone the repository:
   git clone https://github.com/dpant1s/capstone-spring-2026.git

2. Navigate to the project folder:
   cd capstone-spring-2026

3. Install dependencies:
   pip install -r requirements.txt

4. Run the Flask application:
   python app.py

5. Open in browser:
   http://127.0.0.1:5000/

Note: This is a basic MVP backend setup. Full mobile integration (Android/iOS) will be implemented in future sprints.

# Patient User Flow
- Account Creation / Login
- User opens the app
- Creates a new account or logs in with existing credentials
- Device Pairing (Initial Setup)
- User pairs the Bluetooth-enabled medication bottle cap with the app
- Home Dashboard
### A Patient views:
- Medication status (taken, late, missed)
- Butterfly Bucks (BB) balance
- Current game stage
- Medication Tracking
- User takes medication
- Bottle cap sends a Bluetooth signal to the app
- App logs timestamp and updates adherence status
- Reward System
  - App awards Butterfly Bucks based on adherence:
    - On-time → +2 BB
    - Late → +1 BB
    - Missed → 0 BB
- Game Progression
- User earns BB and progresses through stages:
  - Chrysalis → Caterpillar → Butterfly
- User unlocks customization and features
- Progress & History
- User views adherence history
- User views Butterfly Bank (visual rewards)
