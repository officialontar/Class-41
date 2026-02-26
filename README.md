# 🧑‍💼 Django Job Portal System

![Django](https://img.shields.io/badge/Django-4.x-green?logo=django)
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.x-38B2AC?logo=tailwind-css)
![Status](https://img.shields.io/badge/Project-Completed-success)
![License](https://img.shields.io/badge/License-Educational-blue)

A modern and responsive **Job Portal System** built using **Django** and **Tailwind CSS**.  
This project demonstrates full CRUD functionality, dynamic job browsing, search, and sorting system with clean UI design.

---

## 🌐 Live Demo

🚀 _Coming Soon..._  
(You can deploy this project on Render / Railway / PythonAnywhere)

---

## 🧠 Project Topic
📚 Django Job Portal System

---

## ✨ Core Features

### ✅ Job Management (CRUD)
- ✔ Add Job  
- ✔ Update Job Information  
- ✔ Delete Job  
- ✔ Upload Company Logo  
- ✔ View Single Job Details  

### ✅ Job Listing System
- ✔ Display All Jobs (Card View)  
- ✔ Display All Jobs (Table View)  

### ✅ Smart Filtering & Sorting
- ✔ Search Jobs (Title, Company, Category, Location)  
- ✔ Sorting Jobs (A → Z / Z → A by Job Title)  

---

## 🚀 Technology Stack

- 🔹 Backend: Django (Python)
- 🔹 Frontend: Tailwind CSS
- 🔹 Database: SQLite
- 🔹 Template Engine: Django Templates
- 🔹 Version Control: Git & GitHub

---

## 📸 Project Screenshots

> Create a folder named `screenshots/` in your project root and add your images there.

### 🟦 Browse Jobs – Card View
![Browse Jobs](screenshots/browse_jobs_card.png)

### 🟩 Search & Not Found Message
![Search Result](screenshots/search_not_found.png)

### 🟨 All Jobs – Table View with Sorting
![Table View](screenshots/all_jobs_table_sort.png)

### 🟪 Add Job Page
![Add Job](screenshots/add_job.png)

### 🟧 Update Job (Auto-filled Data)
![Update Job](screenshots/update_job.png)

### 🟥 Single Job Details
![Single Job](screenshots/single_job_view.png)

---

## ⚙️ Installation & Setup Guide

### 1️⃣ Clone Repository
```bash
git clone https://github.com/officialontar/Class-41.git
cd Class-41
```

---

### 2️⃣ Create Virtual Environment

#### 🔹 Windows
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

#### 🔹 Mac/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

### 4️⃣ Apply Migrations
```bash
python manage.py migrate
```

---

### 5️⃣ Create Superuser (Admin Access)
```bash
python manage.py createsuperuser
```

---

### 6️⃣ Run Development Server
```bash
python manage.py runserver
```

Open in browser:

- 🌐 Main App → http://127.0.0.1:8000/
- 🔐 Admin Panel → http://127.0.0.1:8000/admin/

---

## 📂 Recommended Folder Structure

```
Job_Portal/
│
├── screenshots/
│   ├── browse_jobs_card.png
│   ├── search_not_found.png
│   ├── all_jobs_table_sort.png
│   ├── add_job.png
│   ├── update_job.png
│   └── single_job_view.png
│
├── templates/
├── static/
├── manage.py
└── README.md
```

---

## 🎯 Learning Outcome

This project helped practice:

- CRUD Operations in Django  
- Template Rendering & Context Passing  
- File Upload Handling  
- Dynamic Search & Sorting  
- Responsive UI Design with Tailwind CSS  
- Git & GitHub Version Control  

---

## 👨‍💻 Author

**MD. ANISUJJAMAN ONTAR**  
Aspiring Full Stack Web Developer  
GitHub: https://github.com/officialontar  

---

## 📄 License

This project is developed for **learning, practice, and portfolio purposes**.