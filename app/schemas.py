from pydantic import BaseModel, EmailStr, Field

# ---------- STUDENTS ----------

class StudentBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    email: EmailStr

class StudentCreate(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: int

    class Config:
        orm_mode = True


# ---------- COURSES ----------

class CourseBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)

class CourseCreate(CourseBase):
    pass

class CourseResponse(CourseBase):
    id: int

    class Config:
        orm_mode = True


# ---------- ENROLLMENTS ----------

class EnrollmentBase(BaseModel):
    student_id: int = Field(..., gt=0)
    course_id: int = Field(..., gt=0)

class EnrollmentCreate(EnrollmentBase):
    pass

class EnrollmentResponse(EnrollmentBase):
    id: int

    class Config:
        orm_mode = True

