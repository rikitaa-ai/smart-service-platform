# Smart Service Request & Approval Platform

A web-based service application portal where users can apply for government-style services and officers can review applications, verify documents, and approve or reject applications.

## Features

### User
- User login with JWT authentication
- Apply for different services
- View submitted applications
- View application status
- Track application workflow

### Officer
- Officer login
- View all applications
- Review applications
- Verify submitted documents
- Approve applications
- Reject applications

## Services

- Business License
- Driving Licence
- Caste Certificate
- Residence Certificate
- Income Certificate
- Birth Certificate
- Death Certificate
- Marriage Certificate
- Domicile Certificate
- Trade License

## Application Workflow

SUBMITTED
→ UNDER_REVIEW
→ DOCUMENT_VERIFIED
→ APPROVED

Applications can also be REJECTED when requirements are not satisfied.

## Technology Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication
- Bootstrap
- HTML
- CSS
- JavaScript
- Swagger / OpenAPI
- Git & GitHub

## User Roles

### USER
Can submit and view their own applications.

### OFFICER
Can view applications, review them, verify documents, and approve or reject them.

### ADMIN
Django administrative access.

## Project Structure

smart-service-platform/
├── accounts/
├── applications/
├── config/
├── templates/
├── manage.py
└── README.md

## How to Run

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
