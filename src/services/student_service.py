from data.storage import load_students, save_students
from exceptions.custom_exceptions import StudentNotFoundError
from models.student import Student
from utils.validators import (
    validate_age,
    validate_grade,
    validate_id,
    validate_name,
    validate_unique_id,
)


class StudentService:
    def __init__(self):
        self.students = load_students()

    def _find_student(self, student_id: int) -> Student:
        for student in self.students:
            if student.student_id == student_id:
                return student
        raise StudentNotFoundError(student_id)

    def add_student(self, student_id_text: str, name: str, age_text: str, grade: str) -> Student:
        student_id = validate_id(student_id_text)
        validate_unique_id(student_id, self.students)
        student = Student(
            student_id=student_id,
            name=validate_name(name),
            age=validate_age(age_text),
            grade=validate_grade(grade),
        )
        self.students.append(student)
        save_students(self.students)
        return student

    def update_student(self, student_id_text: str, name: str = "", age_text: str = "", grade: str = "") -> Student:
        student = self._find_student(validate_id(student_id_text))
        # Blank input means "keep the current value"
        if name.strip():
            student.name = validate_name(name)
        if age_text.strip():
            student.age = validate_age(age_text)
        if grade.strip():
            student.grade = validate_grade(grade)
        save_students(self.students)
        return student

    def delete_student(self, student_id_text: str) -> Student:
        student = self._find_student(validate_id(student_id_text))
        self.students.remove(student)
        save_students(self.students)
        return student

    def search_students(self, keyword: str) -> list[Student]:
        keyword = keyword.strip().lower()
        if not keyword:
            raise ValueError("Search keyword cannot be empty.")
        return [
            student
            for student in self.students
            if keyword in student.name.lower() or keyword == str(student.student_id)
        ]

    def list_students(self) -> list[Student]:
        return self.students