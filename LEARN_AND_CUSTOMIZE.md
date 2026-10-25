# How to make this YOURS - Important Read Before Submit

This starter was built to help you **learn and pass the demo**, not to submit blindly.
Your evaluator will ask you to **demonstrate live** and **explain architecture** (assignment p.2 §08).
If you can't explain it, you won't pass — even if code works.

## 1. You MUST understand these 5 files (5 minutes each)

- **config.py**: Why we use `.env`? → So secrets not on GitHub. `extra="ignore"` ignores extra keys.
- **database.py**: What is `engine`? → connection to SQLite file. `get_db()` gives session per request.
- **model.py**: Each attribute = column. `primary_key=True` = unique ID. Why `nullable=True` for course? → optional per PDF.
- **schemas.py**: Pydantic validates input → wrong email = 422 error. Why `Optional`? → update needs partial fields.
- **routes/students.py**: Read `create_student` line by line — `db.add()` → `commit()` → `refresh()`.

## 2. Personalize in 10 minutes (makes it look like your work)

1. **Change dummy data:** In Swagger, create 3 students with YOUR college names, YOUR course (e.g., MCA, B.Tech AI), YOUR city. Don't keep generic forever.
2. **Edit README:** Replace `[REPLACE WITH YOUR NAME]` at top, update GitHub URL, add 1-2 screenshots of YOUR `/docs` runs.
3. **Add one small feature YOU choose:** e.g., add `GET /students?enrollment_date=2026-09-22` or change error message wording. Mention this in demo — shows you understood.
4. **Practice explaining:** Record yourself saying: “I used FastAPI because… I chose SQLite because…”

## 3. Run it YOURSELF before pushing

Don't just push — run:

```
python -m uvicorn main:app --reload
# open http://localhost:8000/docs
# Create → List → Get 1 → Update 1 → Delete 1 → List again
```

If all 5 return correct codes, screenshot them. Add to README or keep ready for evaluator.

## 4. About Ollama bonus

You asked for Ollama — it's included as `POST /ask`. But:
- Your evaluator can test CRUD **without** Ollama — fallback works
- To test full AI: `ollama serve` in one terminal, `ollama pull llama3.2:1b` in another, then `POST /ask`
- If your laptop is slow, it's okay to NOT demo Ollama — PDF says CRUD alone passes

## 5. Academic Integrity Note

EWB expects you to **be ready to demonstrate and explain** (PDF p.2 §08). Submitting code you can't explain is a risk.
Use this starter as a **learning template**: run it, change it, break it and fix it, then submit YOUR version you understand.

Good luck — you got this! After you run it once, you'll be able to answer any interview question.

