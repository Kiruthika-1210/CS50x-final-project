# SkillTimey – Your Personal Growth Dashboard
#### Video Demo: https://1drv.ms/v/c/84de2954ee5e97ad/ER9oRZeF1hNDtUfUwAhIHjcBFkCSRSl_QNvEdg-k-sIaew?e=lsd9u8
---

### Description:

**SkillTimey** is a web-based personal growth dashboard tailored for students to track learning goals, reflect on their interests, manage academic progress, and receive personalized suggestions for development. Built as my final project for **CS50x**, this platform draws directly from what I’ve learned about full-stack web development using Python, Flask, SQL, HTML, CSS, JavaScript, and Bootstrap.

SkillTimey is designed to address a real problem: the lack of a structured, encouraging space for students to plan and track their growth outside of formal education systems. With SkillTimey, students can:

- Register and log in securely
- Set up a dynamic profile (course, academic year, CGPA, interests, etc.)
- View a personalized dashboard
- Track daily goals
- Monitor skills and learning areas
- Edit their profile anytime via settings
- Logout securely

---

### File Breakdown:

#### `app.py`
- The main Flask application file.
- Handles all routing, logic, database queries, session management.
- Uses `flask_session` and `cs50.SQL` for persistent state and DB access.

#### `templates/`
All frontend HTML templates using Jinja2 templating syntax.

- `layout.html` – Global template layout used by all other pages.
- `home.html` – The homepage with project description and access links.
- `register.html` – User registration form.
- `login.html` – User login form.
- `profile.html` – Intelligent onboarding form that adjusts based on course selection (e.g., hiding/showing CGPA, academic year, etc.).
- `dashboard.html` – Main user hub after login, showing user profile summary and quick access to feature cards.
- `goals.html` – A simple, structured list of motivational and academic goals.
- `skills.html` – A structured skill-level tracker. Users can visually reflect on progress.
- `suggestions.html` – Personalized advice based on selected course and interests.
- `settings.html` – Users can update their nickname, CGPA, interests, and year.

#### `static/style.css`
- Custom CSS file for styling all pages.
- Overrides Bootstrap for brand consistency.
- Ensures all pages are center-aligned, spaced evenly, and use a consistent font and gradient background.

#### `skillTimey.db`
- SQLite database.
- Contains two tables: `users` (username and password) and `profiles` (user ID, nickname, course, year, qualification, CGPA, interests).
- All form submissions are persisted here.

---

### Design Decisions:

- **Dynamic Profile Setup**
  I wanted the registration experience to be simple. So the basic register page only asks for a username and password, and after successful registration, users are routed to a dynamic profile setup form. This separates authentication from personalization, which is a common UX best practice.

- **Course-Based Logic**
  Based on the user’s selected course (e.g., Arts, Engineering, Medicine), certain fields are conditionally shown or hidden. For example, CGPA and academic year are not asked if the user selects “Other.” This minimizes irrelevant input and simplifies the form.

- **Simple Yet Effective Dashboard**
  Instead of overwhelming users with data, I used four main cards:
  - Goals
  - Skills
  - Suggestions
  - Settings
  Each card leads to a focused subpage, keeping the interface clean and encouraging discovery without confusion.

- **Logout Flow**
  The logout button is visually consistent with other CTAs (styled same as login/register). It’s placed at the bottom of the dashboard to make exit intuitive and safe.

---

### Learning Reflection:

Through building SkillTimey, I implemented everything I’ve learned in CS50x — including Python programming, SQL queries, HTML/CSS styling, session handling, templating with Jinja, JavaScript DOM manipulation, and designing RESTful routes. Every route and page was written by me. AI tools like ChatGPT were used **only** for guidance, reviewing logic, and brainstorming — but **not** for direct copy-paste coding. All code is my own work, carefully debugged and tested.

I’m particularly proud of:
- The dynamic logic in the profile setup form
- The visual consistency and layout
- The clean separation between authentication, personalization, and dashboard functionality

---

### Usage Instructions:

1. Install dependencies:
   ```bash
   pip install flask flask-session cs50

2. Run the application:
   flask run

3.Visit:
   http://127.0.0.1:5000

Acknowledgements:

    ChatGPT was used for brainstorming UI structure and validating design decisions.
    All code was authored, tested, and structured by me.

    CS50x — Thank you for such a powerful course. This project was a joy to build and is just the beginning of my developer journey.
