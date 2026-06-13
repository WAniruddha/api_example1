from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running"}

@app.get("/add")
def add(x: float, y: float):
    return {"result": x + y}

@app.get("/subtract")
def subtract(x: float, y: float):
    return {"result": x - y}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 9321))
    uvicorn.run("app:app", host="0.0.0.0", port=port)
