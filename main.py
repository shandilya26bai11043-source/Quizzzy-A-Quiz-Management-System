# QUIZZZY program entry point.
from student_login import register_student, login_student
from quiz_management import run_quiz
from score_calculation import show_result
from validation import read_choice


def main():
    print("QUIZZZY - Online Quiz and Performance Analysis System")
    while True:
        print("\n1. Register")
        print("2. Login and take quiz")
        print("3. Exit")
        choice = read_choice("Choose an option: ", 1, 3)

        if choice == 1:
            register_student()
        elif choice == 2:
            student = login_student()
            if student is not None:
                answers = run_quiz()
                show_result(student["name"], answers)
        else:
            print("Thank you for using QUIZZZY.")
            break


if __name__ == "__main__":
    main()
