from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter(
    prefix="/enrollments",
    tags=["Enrollments"]
)

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -------------------------
# CREAR ENROLLMENT
# -------------------------
@router.post("/", response_model=schemas.EnrollmentResponse)
def create_enrollment(
    enrollment: schemas.EnrollmentCreate,
    db: Session = Depends(get_db)
):
    # Validar que el estudiante exista
    student = crud.get_student_by_id(db, enrollment.student_id)
    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    # Validar que el curso exista
    course = crud.get_course_by_id(db, enrollment.course_id)
    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return crud.create_enrollment(db, enrollment)


# -------------------------
# LEER TODOS LOS ENROLLMENTS
# -------------------------
@router.get("/", response_model=list[schemas.EnrollmentResponse])
def read_enrollments(db: Session = Depends(get_db)):
    return crud.get_enrollments(db)


# -------------------------
# LEER ENROLLMENT POR ID
# -------------------------
@router.get("/{enrollment_id}", response_model=schemas.EnrollmentResponse)
def read_enrollment(
    enrollment_id: int,
    db: Session = Depends(get_db)
):
    enrollment = crud.get_enrollment_by_id(db, enrollment_id)
    if not enrollment:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )
    return enrollment
