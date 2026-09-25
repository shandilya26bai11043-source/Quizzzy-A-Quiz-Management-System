# Major module 2: Quiz Management.
from questions import QUESTIONS
from validation import read_choice


def run_quiz():
    answers = [0] * len(QUESTIONS)
    position = 0

    while position < len(QUESTIONS):
        question = QUESTIONS[position]
        print("\nQuestion", position + 1, "of", len(QUESTIONS))
        print(question["question"])
        for number in range(len(question["options"])):
            print(str(number + 1) + ".", question["options"][number])

        print("Enter 1 to 4 to answer. Enter 5 to go to the previous question.")
        choice = read_choice("Your choice: ", 1, 5)
        if choice == 5:
            if position > 0:
                position = position - 1
            else:
                print("You are already at the first question.")
        else:
            answers[position] = choice
            position = position + 1

    return answers
