from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Logging Middleware")

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Logging Middleware API is running"}