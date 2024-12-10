import pytest
from main import Session, Students, Courses, UpdateInfo

@pytest.fixture(scope="module")
def db_session():
    session = Session()
    yield session
    session.close()

def test_add_student(db_session):
    student = Students(name="Test Student")
    db_session.add(student)
    db_session.commit()

    fetched_student = db_session.query(Students).filter_by(name="Test Student").first()
    assert fetched_student is not None
    assert fetched_student.name == "Test Student"

def test_update_student_name(db_session):
    manager = UpdateInfo(db_session)
    result = manager.update_student_name("Test Student", "Updated Student")

    updated_student = db_session.query(Students).filter_by(name="Updated Student").first()
    assert "updated from Test Student to Updated Student" in result
    assert updated_student.name == "Updated Student"

def test_delete_student(db_session):
    manager = UpdateInfo(db_session)
    result = manager.delete_student("Updated Student")

    deleted_student = db_session.query(Students).filter_by(name="Updated Student").first()
    assert "has been deleted" in result
    assert deleted_student is None
