# Employee Management System – Django REST API

## 📌 Project Overview

This project is a **Django REST Framework (DRF) based CRUD application** designed to manage employee data efficiently.
It demonstrates backend development skills including RESTful API design, JWT authentication, permissions, validation, and pagination.

The application allows authenticated users to create, view, update, and delete employee records securely.

---

## 🛠️ Technologies Used

* **Backend:** Python, Django, Django REST Framework
* **Authentication:** JWT (JSON Web Token)
* **Database:** SQLite (default)
* **Tools:** Git, GitHub, VS Code, PostMan

---

## ✨ Features

* JWT-based authentication
* Employee CRUD operations
* Secure API access using permissions
* Pagination for list APIs
* Search and filtering support
* Proper validation and error handling
* Django Admin panel support

---

## ⚙️ Setup Instructions (Run Locally)

### 1️⃣ Clone and Open the Project

```bash
git clone https://github.com/SANTHOSH12072001/CRUD_DRF.git
cd employee_management
```

### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv env
env\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create Superuser (Optional – for Admin Access)

```bash
python manage.py createsuperuser
```

### 6️⃣ Run the Development Server

```bash
python manage.py runserver
```

The application will run at:

```
http://127.0.0.1:8000/
```

---

## 🔐 Authentication (JWT)

This project uses **JWT Authentication**.

### Obtain Token

```http
POST /api/token/
```

### Refresh Token

```http
POST /api/token/refresh/
```

### Authorization Header

```http
Authorization: Bearer <access_token>
```

---

## 📡 API Documentation

### 🔹 Employee APIs

| Method | Endpoint             | Description               |
| ------ | -------------------- | ------------------------- |
| GET    | /api/employees/      | List all employees        |
| POST   | /api/employees/      | Create a new employee     |
| GET    | /api/employees/{id}/ | Retrieve employee details |
| PUT    | /api/employees/{id}/ | Update employee           |
| DELETE | /api/employees/{id}/ | Delete employee           |

---

## 👨‍💻 Admin Panel

Admin panel is available at:

```
http://127.0.0.1:8000/admin/
```

Use superuser credentials to manage users and employee data.

---

## 🌐 Live Demo

```
Not deployed – Project can be run locally using the setup instructions above.
```

---

## 📁 GitHub Repository

```
https://github.com/SANTHOSH12072001/CRUD_DRF
```

---

## 📝 Notes

* Ensure virtual environment is activated before running the project
* JWT token is required for protected APIs
* Project follows Django best practices

---

## 👤 Author

**Santhosh**
Python & Django Developer
