from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey
from datetime import datetime
from .db import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    company = Column(String)
    location = Column(String)
    description = Column(Text)
    skills = Column(Text)
    source = Column(String)
    url = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


class ResumeProfile(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    skills = Column(Text)
    experience_years = Column(Integer)
    raw_text = Column(Text)


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey("jobs.id"))
    status = Column(String)
    match_score = Column(Float)
    notes = Column(Text)
