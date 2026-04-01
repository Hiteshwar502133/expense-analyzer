# 💰 Smart Expense Analyzer with AI Insights

A powerful Django REST API that tracks expenses, automatically categorizes them, and provides intelligent financial insights.

---

## 🚀 Features

- 🔐 JWT Authentication
- 💸 Expense Tracking (CRUD APIs)
- 🤖 AI-based Category Detection
- 📊 Spending Analytics
- 🧠 Smart Insights & Suggestions

---

## 📸 Demo

### Expenses API
![Expenses](expenses-api.png)

### Insights API
![Insights](insights-api.png)

---

## 🛠 Tech Stack

- Python
- Django
- Django REST Framework
- JWT Authentication

---

## 📡 API Endpoints

| Endpoint | Description |
|--------|------------|
| /api/login/ | Get JWT token |
| /api/expenses/ | Manage expenses |
| /api/analytics/ | Expense breakdown |
| /api/insights/ | AI insights |

---

## 🌐 Live API

Base URL:
https://expense-analyzer-n1mc.onrender.com/

### Endpoints
- /api/login/
- /api/expenses/
- /api/insights/

---

## 🔐 Authentication

Use Bearer Token:

Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc1MDI4NTMzLCJpYXQiOjE3NzUwMjQ5MzMsImp0aSI6Ijc0Y2I0M2ZlOGQ3MTQwMDZhOGUyYzQ5MTllYjQwYzcxIiwidXNlcl9pZCI6IjEifQ.6IUrk4eOs_z2azDGYD8Ig86Q4LGYrxkbcrr1gjITY5E

---

POST /api/login/

{
  "username": "Hitesh",
  "password": "1234"
}

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
python manage.py runserver
