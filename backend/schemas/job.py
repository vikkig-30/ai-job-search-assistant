from pydantic import BaseModel

class JobCreate(BaseModel):
    title: str
    company: str
    location: str
    description: str
    skills: str
    source: str
    url: str

class JobOut(JobCreate):
    id: int

    class Config:
        from_attributes = True
