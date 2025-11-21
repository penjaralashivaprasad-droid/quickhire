# QuickHire — Job Post & Apply API (Django + DRF)

## Overview
QuickHire is a simple job portal backend built with Django and Django REST Framework.
Employers can post jobs; applicants can view and apply. JWT (SimpleJWT) is used
for authentication.

## What's included
- Django project `quickhire`
- Apps: `accounts`, `jobs`
- SQLite database (empty) `db.sqlite3` created when you run migrations
- Postman collection `postman_quickhire.json`
- `requirements.txt`

## Setup (from scratch)
1. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS / Linux
   venv\Scripts\activate    # Windows
   ```
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations and create a superuser:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
4. Run the server:
   ```bash
   python manage.py runserver
   ```
5. API root: `http://127.0.0.1:8000/api/`

## Key endpoints
- `POST /api/register/` — register user (role: "employer" or "applicant")
- `POST /api/token/` — get JWT (access + refresh)
- `GET /api/jobs/` — list/search jobs (auth required)
- `POST /api/jobs/` — create job (employer only)
- `PUT /api/jobs/{id}/` — update job (employer only)
- `DELETE /api/jobs/{id}/` — delete job (employer only)
- `GET /api/jobs/{id}/applicants/` — employer sees applicants for a job
- `POST /api/apply/` — applicant applies to a job
- `GET /api/myapplications/` — applicant views their applications

## Notes
- Search: use query params `?search=engineer` (searches title) or `?location=Delhi`.
- Admin site at `/admin/` contains job and application overviews.

## Postman
Import `postman_quickhire.json` into Postman to test endpoints quickly.
