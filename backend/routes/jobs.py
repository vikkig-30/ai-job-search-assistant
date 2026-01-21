from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.models import Job
from database.db import SessionLocal
from schemas.job import JobCreate, JobOut

router = APIRouter(prefix="/jobs", tags=["Jobs"])

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST /jobs → create a new job
@router.post("/", response_model=JobOut)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    new_job = Job(**job.dict())
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job

# GET /jobs → fetch all jobs
@router.get("/", response_model=list[JobOut])
def get_jobs(db: Session = Depends(get_db)):
    return db.query(Job).all()
