from exceptions.custom_exceptions import StudentError
from services.student_service import StudentService

MENU = """
==== Student Management System ====
1. Add student
2. View all students
3. Update student
4. Delete student
5. Search students
6. Exit
"""


def print_students(students):
    if not students:
        print("No students found.")
        return
    for student in students:
        print(student)


def handle_add(service):
    student = service.add_student(
        input("Student ID: "),
        input("Name: "),
        input("Age: "),
        input("Grade: "),
    )
    print(f"Added: {student}")


def handle_update(service):
    print("Leave a field blank to keep its current value.")
    student = service.update_student(
        input("Student ID to update: "),
        input("New name: "),
        input("New age: "),
        input("New grade: "),
    )
    print(f"Updated: {student}")


def handle_delete(service):
    student = service.delete_student(input("Student ID to delete: "))
    print(f"Deleted: {student}")


def handle_search(service):
    print_students(service.search_students(input("Search by name or ID: ")))


def main():
    service = StudentService()

    while True:
        print(MENU)
        choice = input("Choose an option (1-6): ").strip()

        if choice == "6":
            print("Goodbye!")
            break

        try:
            if choice == "1":
                handle_add(service)
            elif choice == "2":
                print_students(service.list_students())
            elif choice == "3":
                handle_update(service)
            elif choice == "4":
                handle_delete(service)
            elif choice == "5":
                handle_search(service)
            else:
                print("Invalid option. Please choose 1 to 6.")
        except (ValueError, StudentError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()