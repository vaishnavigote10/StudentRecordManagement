class StudentError(Exception):
    """Base class for all student management errors."""


class StudentNotFoundError(StudentError):
    def __init__(self, student_id):
        super().__init__(f"Student with ID {student_id} not found.")
        self.student_id = student_id


class DuplicateStudentError(StudentError):
    def __init__(self, student_id):
        super().__init__(f"Student with ID {student_id} already exists.")
        self.student_id = student_id