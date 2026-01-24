from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version="0.1.0")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Welcome to the Banking Processing API"}