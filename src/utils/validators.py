from exceptions.custom_exceptions import DuplicateStudentError

MIN_AGE = 5
MAX_AGE = 100
ALLOWED_NAME_CHARS = " .-'"


def validate_id(student_id_text: str) -> int:
    try:
        student_id = int(student_id_text)
    except ValueError:
        raise ValueError("Student ID must be a whole number.")
    if student_id <= 0:
        raise ValueError("Student ID must be a positive number.")
    return student_id


def validate_name(name: str) -> str:
    cleaned = name.strip()
    if not cleaned:
        raise ValueError("Name cannot be empty.")
    if not all(ch.isalpha() or ch in ALLOWED_NAME_CHARS for ch in cleaned):
        raise ValueError("Name can only contain letters, spaces, dots, hyphens, and apostrophes.")
    return cleaned


def validate_age(age_text: str) -> int:
    try:
        age = int(age_text)
    except ValueError:
        raise ValueError("Age must be a whole number.")
    if not MIN_AGE <= age <= MAX_AGE:
        raise ValueError(f"Age must be between {MIN_AGE} and {MAX_AGE}.")
    return age


def validate_grade(grade: str) -> str:
    cleaned = grade.strip().upper()
    if not cleaned:
        raise ValueError("Grade cannot be empty.")
    if len(cleaned) > 3:
        raise ValueError("Grade must be 3 characters or fewer (for example A, B+, or C).")
    return cleaned


def validate_unique_id(student_id: int, students) -> None:
    if any(student.student_id == student_id for student in students):
        raise DuplicateStudentError(student_id)