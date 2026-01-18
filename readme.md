# Employee Management System – Django REST API

 Project Overview

This project is a **Django REST Framework (DRF) based CRUD application** designed to manage employee data efficiently.
It demonstrates backend development skills including RESTful API design, JWT authentication, permissions, validation, and pagination.

The application allows authenticated users to create, view, update, and delete employee records securely.



 Technologies Used

* **Backend:** Python, Django, Django REST Framework
* **Authentication:** JWT (JSON Web Token)
* **Database:** SQLite (default)
* **Tools:** Git, GitHub, VS Code, Post Man



 Features

* JWT-based authentication
* Employee CRUD operations
* Secure API access using permissions
* Pagination for list APIs
* Search and filtering support
* Proper validation and error handling
* Django Admin panel support



 Setup Instructions (Run Locally)

1️ Clone and Open the Project


git clone https://github.com/SANTHOSH12072001/CRUD_DRF.git
cd employee_management


2️ Create and Activate Virtual Environment

python -m venv env
env\Scripts\activate


3️ Install Dependencies

pip install -r requirements.txt


4️ Apply Database Migrations

python manage.py makemigrations
python manage.py migrate


5 Create Superuser (Optional – for Admin Access)


python manage.py createsuperuser


6️ Run the Development Server

python manage.py runserver


The application will run at:

http://127.0.0.1:8000/



Authentication (JWT)

This project uses **JWT Authentication**.

Obtain Token


POST /api/token/


Refresh Token

POST /api/token/refresh/


Authorization Header

Authorization: Bearer <access_token>


 API Documentation

### Employee APIs

| Method | Endpoint             | Description               |
| ------ | -------------------- | ------------------------- |
| GET    | /api/employees/      | List all employees        |
| POST   | /api/employees/      | Create a new employee     |
| GET    | /api/employees/{id}/ | Retrieve employee details |
| PUT    | /api/employees/{id}/ | Update employee           |
| DELETE | /api/employees/{id}/ | Delete employee           |



 Admin Panel

Admin panel is available at:


http://127.0.0.1:8000/admin/


Use superuser credentials to manage users and employee data.



Live Demo

Not deployed – Project can be run locally using the setup instructions above.



 GitHub Repository


https://github.com/SANTHOSH12072001/CRUD_DRF




 📝 Notes

* Ensure virtual environment is activated before running the project
* JWT token is required for protected APIs
* Project follows Django best practices



 Author

**Santhosh**
Python & Django Developer
