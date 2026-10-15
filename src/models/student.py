class Student:
    def __init__(self, student_id: int, name: str, age: int, grade: str):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade,
        }

    def __str__(self):
        return f"ID: {self.student_id} | {self.name} | Age: {self.age} | Grade: {self.grade}"