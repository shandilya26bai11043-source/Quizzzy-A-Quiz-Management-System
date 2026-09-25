# Simple checks for input validation and score calculation.
from validation import valid_name, valid_student_id, valid_password
from score_calculation import calculate_score
from questions import QUESTIONS


def run_tests():
    assert valid_name("Riya")
    assert not valid_name(" ")
    assert valid_student_id("STU01")
    assert not valid_student_id("A")
    assert valid_password("abcd")
    assert not valid_password("abc")

    all_correct = []
    for question in QUESTIONS:
        all_correct.append(question["answer"])
    correct, total, percentage = calculate_score(all_correct)
    assert correct == total
    assert percentage == 100

    all_wrong = [0] * len(QUESTIONS)
    correct, total, percentage = calculate_score(all_wrong)
    assert correct == 0
    assert percentage == 0
    print("All simple checks passed.")


if __name__ == "__main__":
    run_tests()
