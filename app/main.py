from fastapi import FastAPI
from app.database import engine, Base
from app import models 

from app.routers import students, courses, enrollments

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(students.router)
app.include_router(courses.router)
app.include_router(enrollments.router)

@app.get("/")
def root():
    return {"message": "API is running"}
