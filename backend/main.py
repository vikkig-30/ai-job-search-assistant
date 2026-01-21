from fastapi import FastAPI
from database.db import engine
from database.models import Base
from routes.jobs import router as jobs_router




app = FastAPI(title="AI Job Search Assistant")
app.include_router(jobs_router)

# Create database tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"status": "running"}
