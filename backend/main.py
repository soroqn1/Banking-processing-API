from fastapi import FastAPI

app = FastAPI(title="Banking Processing API", version="0.1.0")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Welcome to the Banking Processing API"}