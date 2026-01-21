from fastapi import FastAPI
from database.db import engine
from database.models import Base

Base.metadata.create_all(bind=engine)


app = FastAPI(title="AI Job Search Assistant")

@app.get("/")
def home():
    return {"status": "running"}
