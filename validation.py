# Small input checks shared by the project.

def clean_name(name):
    return name.strip()


def valid_name(name):
    return len(clean_name(name)) >= 2


def valid_student_id(student_id):
    return len(student_id.strip()) >= 3


def valid_password(password):
    return len(password) >= 4


def read_choice(prompt, low, high):
    while True:
        value = input(prompt).strip()
        try:
            number = int(value)
            if number >= low and number <= high:
                return number
            print("Enter a number from", low, "to", high)
        except ValueError:
            print("Please enter a whole number")
