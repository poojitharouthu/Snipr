Snipr - URL Shortener
Snipr is a minimal and elegant URL shortener web application built with Flask and designed with a fully custom UI.
It generates short, shareable links, stores them in a database, and includes smooth UX features such as link copying and quick reset.

Features:
Generate short URLs instantly
SQLite database storage
One-click “Copy Link” button
State-based UI (SNIP IT → COPY LINK → COPIED)
Custom-designed frontend using unique fonts & styling
Responsive layout
Reusable and easy to extend

Tech Stack:
Python (Flask) - backend logic & routing
SQLite - database for storing URLs
HTML, CSS, JavaScript - frontend
Fonts - Brick Sans, Bricolage Grotesque, Norwester

Project Structure:
snipr/
│── app.py
│── requirements.txt
│── snipr.db
│
├── static/
│   ├── style.css
│   └── fonts/
│       ├── NTBrickSans.ttf
│       ├── norwester.otf
│       └── BricolageGrotesque.ttf
│
└── templates/
    └── index.html

How to Run:
1. Download or clone the project
2. Install Python + Flask
3. Run the app: python app.py
4. Open in browser: http://127.0.0.1:5000

