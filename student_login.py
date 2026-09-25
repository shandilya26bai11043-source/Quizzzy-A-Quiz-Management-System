# Major module 1: Student Login.
from data_store import load_students, save_students
from validation import clean_name, valid_name, valid_student_id, valid_password


def register_student():
    print("\nStudent Registration")
    name = clean_name(input("Full name: "))
    student_id = input("Student ID: ").strip()
    password = input("Create password (at least 4 characters): ")

    if not valid_name(name):
        print("Name must contain at least 2 characters.")
        return False
    if not valid_student_id(student_id):
        print("Student ID must contain at least 3 characters.")
        return False
    if not valid_password(password):
        print("Password must contain at least 4 characters.")
        return False

    students = load_students()
    for student in students:
        if student["student_id"].lower() == student_id.lower():
            print("That Student ID is already registered.")
            return False

    student = {"name": name, "student_id": student_id, "password": password}
    students.append(student)
    if save_students(students):
        print("Registration complete. You can now log in.")
        return True
    return False


def login_student():
    print("\nStudent Login")
    student_id = input("Student ID: ").strip()
    password = input("Password: ")
    students = load_students()

    for student in students:
        if student["student_id"].lower() == student_id.lower():
            if student["password"] == password:
                print("Welcome,", student["name"])
                print("Student ID:", student["student_id"])
                return student
            print("Password is incorrect.")
            return None
    print("Student ID was not found. Register first.")
    return None
