from fastapi import FastAPI
from app.db.database import init_db
from app.routers import math

init_db()

app = FastAPI(title="Math API")

app.include_router(math.router)
