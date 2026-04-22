````md
# 🎓 AI Attendance System

An advanced **AI-powered Attendance Management System** built with **Python + Streamlit** that automates attendance using **Face Recognition**, **Voice Verification**, and **Smart Subject Management**.

Designed for modern schools, colleges, coaching institutes, and smart classrooms.

---

## 🚀 Features

## 👨‍🏫 Teacher Panel

- Secure Teacher Login / Registration
- Create & Manage Subjects
- Generate Subject Join Codes
- Share Subject Codes via QR Code
- Add Classroom Photos
- AI Face Detection from Group Photos
- Voice Attendance System
- Attendance Records Dashboard
- Present / Absent Reports
- Student Enrollment Management

---

## 🎓 Student Panel

- FaceID Login
- Auto Registration for New Students
- Voice Enrollment (Optional)
- Join Subjects via Invite Code
- Auto Enroll through URL Query Params
- View Enrolled Subjects
- Attendance Statistics
- Unenroll from Subjects
- Fast Secure Login

---

## 🤖 AI Features

### 👁 Face Recognition

- Detects Faces from Camera / Photos
- Identifies Registered Students
- Supports Multiple Students in Classroom Photos
- Embedding Based Recognition

### 🎤 Voice Recognition

- Voice Embedding Verification
- Voice-only Attendance Support
- Speaker Identity Matching

### ⚡ Smart Automation

- Auto Attendance Marking
- Instant Reports
- Live Photo Analysis
- Duplicate Prevention

---

## 🛠 Tech Stack

| Technology | Usage |
|----------|------|
| Python | Backend Logic |
| Streamlit | Frontend UI |
| NumPy | Image Arrays |
| Pandas | Data Processing |
| Pillow | Image Handling |
| Supabase | Database + Cloud Backend |
| Face Recognition / Embeddings | AI Attendance |
| Voice Embeddings | Voice Authentication |

---

## 📂 Project Structure

```bash
AI-ATTENDANCE SYSTEM/
│── app.py
│── requirements.txt
│── README.md
│── .streamlit/
│   └── secrets.toml
│
└── src/
    ├── components/
    ├── database/
    ├── pipelines/
    ├── screens/
    └── ui/
````

---

## 📌 Main Modules

### 📍 Components

Reusable UI components:

* Header
* Footer
* Subject Cards
* Dialog Boxes
* QR Share Popup
* Attendance Result Popup

### 📍 Database

Supabase integration:

* Students Table
* Teachers Table
* Subjects Table
* Attendance Logs
* Enrollments

### 📍 Pipelines

AI Processing modules:

* Face Pipeline
* Voice Pipeline

### 📍 Screens

* Home Screen
* Teacher Dashboard
* Student Dashboard

---

## 🔐 Authentication System

### Teacher

* Username + Password Login
* Registration
* Session Management

### Student

* Face Recognition Login
* Auto New User Registration

---

## 📸 Attendance Workflow

1. Teacher selects subject
2. Uploads classroom photos
3. AI scans all faces
4. Matches registered students
5. Marks attendance automatically
6. Saves logs to database

---

## 🎤 Voice Attendance Workflow

1. Teacher starts voice attendance
2. Student speaks registered phrase
3. Voice embedding matched
4. Attendance marked instantly

---

## 🌟 Why This Project?

Traditional attendance systems are:

❌ Slow
❌ Manual
❌ Proxy-prone
❌ Time consuming

This system solves all with AI.

✅ Fast
✅ Accurate
✅ Contactless
✅ Smart
✅ Secure

---

## 📈 Future Enhancements

* Live CCTV Attendance
* WhatsApp Alerts
* Excel Export
* Email Reports
* Admin Dashboard
* Mobile App
* Cloud Deployment
* Multi College Support
* Anti Spoof Face Detection

---

## ▶️ Run Locally

```bash
git clone <your-repo-url>
cd AI-ATTENDANCE-SYSTEM
pip install -r requirements.txt
streamlit run app.py
```

---

## 🔑 Environment Setup

Create:

```toml
.streamlit/secrets.toml
```

Add:

```toml
SUPABASE_URL=your_url
SUPABASE_KEY=your_key
```

---

## 👨‍💻 Developed By

**Vaibhav Soni**

AI Developer | Python Developer | Full Stack Builder

---

## 💎 Project Highlights

✔ Real World Problem Solving
✔ AI + Web Integration
✔ Production Ready Structure
✔ Clean Code Architecture
✔ Modern UI
✔ Fast Performance

---

## 📜 License

Open Source for Learning & Educational Use.

---

# ⭐ If you like this project give it a star!

```
```
