# Campus Learning Portal

Django web app for campus courses, student accounts, profiles, and learning content — built for an academic / college learning experience.

## Features

- Course catalog and landing pages
- Student / user accounts with profiles and settings
- Internal mail between users
- Admin setup commands for seeding campus content
- PostgreSQL-ready (SQLite fine for local development)
- Gunicorn config for production-style deploys

## Requirements

- Python **3.12** (recommended for `requirements-latest.txt`)
- PostgreSQL (optional for local; update credentials if you use it)

## Quick start

### 1) Create and activate environment

```powershell
py -3.12 -m venv .venv312
.\.venv312\Scripts\Activate.ps1
```

### 2) Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements-latest.txt
```

### 3) Migrate and run

```powershell
python "CampusLearningPortal_project\manage.py" check
python "CampusLearningPortal_project\manage.py" migrate
python "CampusLearningPortal_project\manage.py" runserver
```

Open: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Notes

- If PostgreSQL credentials differ, update `CampusLearningPortal_project\campus_learning_portal\settings.py` (or your secret settings file from `secret_settings_example.py`).
- Optional seed command: `python CampusLearningPortal_project\manage.py setup_vssutlearning`
- Keep this project on Python 3.12 for the dependency set in `requirements-latest.txt`.

## Tech stack

- Django
- PostgreSQL / SQLite
- Gunicorn
