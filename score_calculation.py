# Major module 3: Score Calculation.
from questions import QUESTIONS


def calculate_score(answers):
    correct = 0
    for index in range(len(QUESTIONS)):
        if answers[index] == QUESTIONS[index]["answer"]:
            correct = correct + 1
    total = len(QUESTIONS)
    percentage = (correct / total) * 100
    return correct, total, percentage


def show_result(student_name, answers):
    correct, total, percentage = calculate_score(answers)
    print("\nFinal Result")
    print("Student:", student_name)
    print("Marks:", str(correct) + " out of " + str(total))
    print("Percentage:", str(round(percentage, 2)) + "%")
    return correct, total, percentage
