# main.py - entry point for FastAPI app
# Day 7-9: This file creates app and connects routers

from fastapi import FastAPI
from app.database import engine, Base
from app.routes import students, ai_query

# Create tables in database (if not exists)
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title="EWB Students Database CRUD API",
    description="Internship Project - Students Database with CRUD + Optional Ollama AI",
    version="1.0.0"
)

# Include routers
app.include_router(students.router)
app.include_router(ai_query.router)

# Root endpoint
@app.get("/")
def read_root():
    return {
        "message": "Welcome to Students Database CRUD API",
        "docs": "Visit /docs for Swagger UI",
        "endpoints": [
            "POST /students - Create student",
            "GET /students - List students",
            "GET /students/{id} - Get one student",
            "PUT /students/{id} - Update student",
            "DELETE /students/{id} - Delete student",
            "POST /ask - Ask AI about students (bonus)"
        ]
    }

# Health check
@app.get("/health")
def health_check():
    return {"status": "ok", "database": "connected"}
