Snipr is a minimal and elegant URL shortener web application built with Flask and designed with a fully custom UI. It generates short, shareable links, stores them in a database, and includes smooth UX features such as link copying and quick reset.


Features:
1. Generate short URLs instantly
2. SQLite database storage
3. One-click “Copy Link” button
4. State-based UI (SNIP IT → COPY LINK → COPIED)
5. Custom-designed frontend using unique fonts & styling
6. Responsive layout
7. Reusable and easy to extend


Technologies Used:
Python (Flask) - backend logic & routing
SQLite - database for storing URLs
HTML, CSS, JavaScript - frontend
Fonts - Brick Sans, Bricolage Grotesque, Norwester


Project Structure:

```
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
```


How to Run:
1. Download or clone the project
2. Install Python + Flask
3. Run the app: python app.py
4. Open in browser: http://127.0.0.1:5000


Author: Poojitha Routhu Github: https://github.com/poojitharouthu


If you like this project, feel free to star the repo or fork it to build your own version!

