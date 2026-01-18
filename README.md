# Candidate Job Portal – Django Backend

This is the **Django REST API backend** for the Candidate Job Portal project.  
It provides **session-based authentication** (Login / Register / Logout) and connects with a **React (Vite) frontend**.

---

## 🚀 Tech Stack

- Python 3.10+
- Django 4+
- Django REST Framework
- SQLite (default, can be replaced with PostgreSQL/MySQL)
- Session-based Authentication
- CORS enabled for React frontend

---

## 📁 Project Structure

backend/
│── manage.py
│── backend/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ ├── asgi.py
│ └── wsgi.py
│
│── accounts/
│ ├── migrations/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ └── urls.py
│
│── db.sqlite3
└── requirements.txt

