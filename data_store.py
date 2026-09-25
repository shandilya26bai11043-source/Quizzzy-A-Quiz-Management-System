# Reads and writes the simple student data file.
import json
import os

DATA_FILE = "students.json"


def load_students():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        file = open(DATA_FILE, "r", encoding="utf-8")
        students = json.load(file)
        file.close()
        if isinstance(students, list):
            return students
        return []
    except (OSError, json.JSONDecodeError):
        print("Student data could not be read. Starting with an empty list.")
        return []


def save_students(students):
    try:
        file = open(DATA_FILE, "w", encoding="utf-8")
        json.dump(students, file, indent=4)
        file.close()
        return True
    except OSError:
        print("Student data could not be saved.")
        return False
