import json
from pathlib import Path

from models.student import Student

# Points to Task-1/student_data.json
DATA_FILE = Path(__file__).resolve().parents[2] / "student_data.json"


def load_students() -> list[Student]:
    if not DATA_FILE.exists():
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            records = json.load(file)
    except json.JSONDecodeError:
        print("Warning: student_data.json is corrupted. Starting with an empty list.")
        return []
    return [Student(**record) for record in records]


def save_students(students: list[Student]) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump([student.to_dict() for student in students], file, indent=4)