API Documentation – Employee Management System

Project Overview
This project is a RESTful API built using Django REST Framework with JWT authentication.
It allows authenticated users to manage employee records.

Technologies Used
- Python
- Django
- Django REST Framework
- SimpleJWT
- SQLite
-PostMan

Steps to Run the Project Locally

1. Clone the Repository
git clone <repository-url>
cd <project-folder>

2. Create Virtual Environment
python -m venv venv

Activate:
Windows: venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Apply Migrations
python manage.py makemigrations
python manage.py migrate

5. Create Superuser (Optional)
python manage.py createsuperuser

6. Run Server
python manage.py runserver

Server URL:
http://127.0.0.1:8000/

JWT Authentication

Obtain Token:
POST /api/token/

Request:
{
  "username": "your_username",
  "password": "your_password"
}
Refresh Token:
POST /api/token/refresh/

Authorization Header:
Authorization: Bearer <access_token>

Employee APIs

Create Employee:
POST /api/employees/

Get Employees (Paginated):
GET /api/employees/?page=1

Get Employee by ID:
GET /api/employees/{id}/

Filter:
/api/employees/?role=IT
/api/employees/?department=HR

Update Employee:
PATCH /api/employees/{id}/

Delete Employee:
DELETE /api/employees/{id}/

Pagination
10 records per page
Example:
GET /api/employees/?page=2

Permissions
Only authenticated users can access APIs.

Conclusion
This API uses JWT authentication, follows REST standards, and supports pagination and filtering.

