from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey, insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

DATABASE_URL = "postgresql://obog:tcamry@localhost/lesson22"

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

class UpdateInfo(Students):
    def __init__(self, session):
        self.session = session

    def update_student_name(self, old_name, new_name):
        student = self.session.query(Students).filter_by(name=old_name).first()
        if student:
            student.name = new_name
            self.session.commit()
            print(f"Student name updated from {old_name} to {new_name}")
        else:
            print(f"Student with name {old_name} not found")

    def update_course_name(self, old_name, new_name):
        course = self.session.query(Courses).filter_by(name=old_name).first()
        if course:
            course.name = new_name
            self.session.commit()
            print(f"Course name updated from {old_name} to {new_name}")
        else:
            print(f"Course with name {old_name} not found")

    def delete_student(self, name):
        student = self.session.query(Students).filter_by(name=name).first()
        if student:
            self.session.delete(student)
            self.session.commit()
            print(f"Student {name} has been deleted.")
        else:
            print(f"Student with name {name} not found")


Session = sessionmaker(bind=engine)
session = Session()

session.add_all([
    Courses(name='Law'),
    Courses(name='Bio'),
    Courses(name='Geo'),
    Courses(name='Journalist'),
    Courses(name='Math'),
    Students(name='John'),
    Students(name='Cat'),
    Students(name='Suzy'),
    Students(name='Len'),
    Students(name='Pavel'),
    Students(name='Alex'),
    Students(name='Mikel'),
    Students(name='Oliver'),
    Students(name='Jack'),
    Students(name='Harry'),
    Students(name='Jacob'),
    Students(name='Charlie'),
    Students(name='Thomas'),
    Students(name='George'),
    Students(name='Oscar'),
    Students(name='James'),
    Students(name='William'),
    Students(name='Margaret'),
    Students(name='Samantha'),
    Students(name='Bethany'),
])
session.commit()

data_to_insert = [
    {"courses_id": 1, "students_id": 1},
    {"courses_id": 2, "students_id": 2},
    {"courses_id": 3, "students_id": 3},
    {"courses_id": 4, "students_id": 4},
    {"courses_id": 5, "students_id": 5},
    {"courses_id": 1, "students_id": 6},
    {"courses_id": 2, "students_id": 7},
    {"courses_id": 3, "students_id": 8},
    {"courses_id": 4, "students_id": 9},
    {"courses_id": 5, "students_id": 10},
    {"courses_id": 1, "students_id": 11},
    {"courses_id": 2, "students_id": 12},
    {"courses_id": 3, "students_id": 13},
    {"courses_id": 4, "students_id": 14},
    {"courses_id": 5, "students_id": 15},
    {"courses_id": 1, "students_id": 16},
    {"courses_id": 2, "students_id": 17},
    {"courses_id": 3, "students_id": 18},
    {"courses_id": 4, "students_id": 19},
    {"courses_id": 5, "students_id": 20},
]
stmt = insert(courses_students).values(data_to_insert)
session.execute(stmt)
session.commit()


Session = sessionmaker(bind=engine)
session = Session()

students = session.query(Students).all()
for student in students:
    print(f"Student: {student.name}")
    for course in student.courses:
        print(f" Linked to: {course.name}")

courses = session.query(Courses).all()
for course in courses:
    print(f"Course: {course.name}")
    for student in course.students:
        print(f" Linked to: {student.name}")


manager = UpdateInfo(session)
manager.update_student_name('John', 'Vasy')
manager.update_course_name('Math', 'Advanced Math')
manager.delete_student('Vasy')

