# EWB Students Database CRUD API

Internship Project - Python Backend Development | EWB Edu Tech Pvt. Ltd.  
**Student:** Vaishnavi Gupta | **Batch:** AI & ML Batch 1 | **Trainer:** Darshil Shukla

> Build a Python backend to manage student records using CRUD with FastAPI + SQLite. Bonus: Local Ollama AI answers questions grounded in DB.

---

## Prerequisites

- Python 3.10 or higher
- VS Code (recommended)
- Git

**Check versions:**
```bash
python --version
pip --version
```

---

## Installation

1. **Clone the repo:**
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

2. **Create virtual environment (Windows):**
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
# You should see (venv) in terminal
```

**For Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Setup environment file:**
```bash
copy .env.example .env
# For Mac/Linux: cp .env.example .env
# Edit .env if needed - default SQLite path works fine
```

---

## Run the Application

```bash
python -m uvicorn main:app --reload
```

- App runs at: `http://localhost:8000`
- Swagger Docs (test here): `http://localhost:8000/docs`
- Root: `http://localhost:8000/`

You should see: `Application startup complete.`

---

## API Endpoints (Mandatory CRUD)

All endpoints are documented in Swagger (`/docs`). These are the 5 suggested endpoints from assignment:

| Method | Endpoint | Purpose | Example Body |
|--------|----------|---------|--------------|
| POST | `/students` | Create student | `{"name":"Aarav Sharma","date_of_birth":"2005-08-12","email":"aarav@test.com","phone":"9876543210","course":"BCA"}` |
| GET | `/students` | List all | `GET /students?course=BCA&search=Aarav` |
| GET | `/students/{id}` | Get one | `GET /students/1` |
| PUT | `/students/{id}` | Update | `{"phone":"9999999999"}` |
| DELETE | `/students/{id}` | Delete | `DELETE /students/1` |

**Sample requests:**

**Create:**
```bash
curl -X POST http://localhost:8000/students -H "Content-Type: application/json" -d "{\"name\":\"Aarav Sharma\",\"date_of_birth\":\"2005-08-12\",\"email\":\"aarav@test.com\",\"course\":\"BCA\"}"
```

**List:**
```bash
curl http://localhost:8000/students
```

---

## Testing via Swagger UI (Recommended for evaluator)

1. Open `http://localhost:8000/docs`
2. Click **POST /students** → Try it out → Paste sample body → Execute → Should get 201
3. Click **GET /students** → Execute → Should list created students
4. Click **GET /students/1** → Execute → Should return single record or 404 if not found
5. Click **PUT /students/1** → Update phone → Execute
6. Click **DELETE /students/1** → Execute → Should return success

All 5 should show correct status codes (201, 200, 404).

---

## Optional Bonus: Local AI with Ollama

This is optional — CRUD alone is sufficient per assignment.

**Setup (one time):**
1. Install Ollama from https://ollama.com
2. Pull model:
```bash
ollama serve
# In new terminal:
ollama pull llama3.2:1b
```
3. Already installed via `requirements.txt`: `langchain-ollama`

**Use:**
- `POST http://localhost:8000/ask` with body `{"question":"How many students are there?"}`
- Also try: `{"question":"List students born after 2005"}`
- Check status: `GET http://localhost:8000/ask/status`

If Ollama not running, the endpoint still returns a fallback answer from DB (so evaluator can still test).

---

## Project Structure

```
student_management/
├── main.py                # App entry point
├── requirements.txt       # Dependencies
├── .env.example           # Example env (push this, not .env)
├── .gitignore
├── app/
│   ├── config.py          # Loads .env via pydantic-settings
│   ├── database.py        # SQLite + SQLAlchemy setup
│   ├── model.py           # Student table definition
│   ├── schemas.py         # Pydantic validation
│   └── routes/
│       ├── students.py    # CRUD endpoints
│       └── ai_query.py    # Bonus AI endpoint
```

This matches Day 7-10 training structure.

---

## Database

- SQLite file: `students.db` (auto-created on first run)
- Persists after restart
- View data: you can add a simple GET endpoint already does this, or use DB Browser for SQLite

---

## Notes

- Dummy data only — no real personal info committed
- `.env` is in `.gitignore` — not pushed to GitHub
- Input validation: email format checked, at least email or phone required, 404 for missing ID

---

## Submission

1. Push to **public GitHub** repo
2. Submit GitHub link via EWB trainer's announced channel (shared Google Drive + WhatsApp)
3. Be ready to demo live: create → list → get → update → delete

---

## Demo Preparation (for viva)

Be able to explain:
- How `config.py` loads `.env`
- Difference between `model.py` (storage) and `schemas.py` (validation)
- How `get_db()` provides DB session
- Why SQLite over Excel (Excel locks, no transactions)
- How AI endpoint fetches records first then gives to model (no raw SQL)

---

Issued by EWB Edu Tech Pvt. Ltd. | Internship Program
