from sqlalchemy.orm import Session
from . import models, schemas

# ---------- STUDENTS ----------

def create_student(db: Session, student: schemas.StudentCreate):
    existing = db.query(models.Student).filter(
        models.Student.email == student.email
    ).first()

    if existing:
        return None

    new_student = models.Student(
        name=student.name,
        email=student.email
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


def get_students(db: Session):
    return db.query(models.Student).all()


def get_student_by_id(db: Session, student_id: int):
    return db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()


# ---------- COURSES ----------

def create_course(db: Session, course: schemas.CourseCreate):
    new_course = models.Course(title=course.title)
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course


def get_courses(db: Session):
    return db.query(models.Course).all()


def get_course_by_id(db: Session, course_id: int):
    return db.query(models.Course).filter(
        models.Course.id == course_id
    ).first()


# ---------- ENROLLMENTS ----------

def create_enrollment(db: Session, enrollment: schemas.EnrollmentCreate):
    student = get_student_by_id(db, enrollment.student_id)
    course = get_course_by_id(db, enrollment.course_id)

    if not student or not course:
        return None

    new_enrollment = models.Enrollment(
        student_id=enrollment.student_id,
        course_id=enrollment.course_id
    )

    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)
    return new_enrollment


def get_enrollments(db: Session):
    return db.query(models.Enrollment).all()

def get_enrollment_by_id(db: Session, enrollment_id: int):
    return db.query(models.Enrollment)\
        .filter(models.Enrollment.id == enrollment_id)\
        .first()

