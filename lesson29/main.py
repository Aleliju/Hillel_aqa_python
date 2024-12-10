from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey, insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

DATABASE_URL = "postgresql://obog:tcamry@postgres-db/lesson22"

engine = create_engine(DATABASE_URL)
Base = declarative_base()

courses_students = Table(
    'courses_students', Base.metadata,
    Column('courses_id', Integer, ForeignKey('Courses_main.id'), primary_key=True),
    Column('students_id', Integer, ForeignKey('Students_main.id'), primary_key=True)
)

class Courses(Base):
    __tablename__ = 'Courses_main'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship("Students", secondary=courses_students, back_populates="courses")

class Students(Base):
    __tablename__ = 'Students_main'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    courses = relationship("Courses", secondary=courses_students, back_populates="students")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

class UpdateInfo:
    def __init__(self, session):
        self.session = session

    def update_student_name(self, old_name, new_name):
        student = self.session.query(Students).filter_by(name=old_name).first()
        if student:
            student.name = new_name
            self.session.commit()
            return f"Student name updated from {old_name} to {new_name}"
        return f"Student with name {old_name} not found"

    def update_course_name(self, old_name, new_name):
        course = self.session.query(Courses).filter_by(name=old_name).first()
        if course:
            course.name = new_name
            self.session.commit()
            return f"Course name updated from {old_name} to {new_name}"
        return f"Course with name {old_name} not found"

    def delete_student(self, name):
        student = self.session.query(Students).filter_by(name=name).first()
        if student:
            self.session.delete(student)
            self.session.commit()
            return f"Student {name} has been deleted."
        return f"Student with name {name} not found"
