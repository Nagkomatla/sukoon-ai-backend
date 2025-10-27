from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="Sukoon AI Backend", version="1.0.0")


@app.get("/")
def read_root():
    return JSONResponse({"message": "Welcome to Sukoon API"})

