import sys
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/add")

def add(x: float, y: float):
    return {"result": x + y}

@app.get("/subtract")
def subtract(x: float, y: float):
    return {"result": x - y}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=9321)
    print ("Server is running on http://localhost:9321")
    
    
    """operation = sys.argv[1]
    x = int(sys.argv[2])
    y = int(sys.argv[3])
    print(f"x:{x}, y:{y}, operation:{operation}")
    print(f"value={add(x, y)}")"""

