from fastapi import FastAPI

from app.routes import router

app = FastAPI(
    title="Vehicle Maintenance Scheduler"
)

app.include_router(router)