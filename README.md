# Campus Learning Portal - Run Guide

## 1) Create and activate environment (Python 3.12)

```powershell
py -3.12 -m venv .venv312
.\.venv312\Scripts\Activate.ps1
```

## 2) Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements-latest.txt
```

## 3) Run Django checks and migrations

```powershell
python "CampusLearningPortal_project\manage.py" check
python "CampusLearningPortal_project\manage.py" migrate
```

## 4) Start development server

```powershell
python "CampusLearningPortal_project\manage.py" runserver
```

Open: http://127.0.0.1:8000/

## Notes

- If PostgreSQL credentials differ, update `CampusLearningPortal_project\campus_learning_portal\settings.py`
  (or your secret settings file).
- Keep this project on Python 3.12 for the latest dependency set in `requirements-latest.txt`.
