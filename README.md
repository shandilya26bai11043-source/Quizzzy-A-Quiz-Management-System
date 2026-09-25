# QUIZZZY - Online Quiz and Performance Analysis System

A beginner-friendly, console-based Python project. QUIZZZY has exactly three major functional modules: Student Login, Quiz Management, and Score Calculation. Supporting files keep each part small and understandable.

## Requirements
- Python 3.8 or newer
- No installation of third-party packages is required

## Files

| File | Purpose |
|---|---|
| `main.py` | Starts the program and connects the three major modules |
| `student_login.py` | Registers students, checks login, and displays student details |
| `quiz_management.py` | Displays questions, records choices, and allows moving backward |
| `score_calculation.py` | Checks answers and displays marks and percentage |
| `questions.py` | Contains the sample multiple-choice questions |
| `data_store.py` | Reads and writes student details in `students.json` |
| `validation.py` | Checks basic input and numeric menu choices |
| `test_quizzzzy.py` | Contains small checks for validation and score calculation |

The data file `students.json` is created automatically after successful registration.

## Run the Program
1. Download or copy the complete `QUIZZZY` folder.
2. Open a terminal in that folder.
3. Run `python main.py` (on some systems use `python3 main.py`).
4. Choose Register and enter a name, student ID, and password.
5. Choose Login and take the quiz.

## Run the Simple Checks
Run `python test_quizzzzy.py`. The expected message is `All simple checks passed.`

## Input Rules
- Name must have at least 2 characters.
- Student ID must have at least 3 characters and must be unique, ignoring letter case.
- Password must have at least 4 characters.
- Menu and answer choices are whole numbers in the displayed range.
- While answering, enter 5 to move to the previous question. At the first question, the request is ignored.

## Sample Quiz Data
Five Python basics questions are included in `questions.py`. Each has four choices and one correct choice.

## Storage
Student records are saved in `students.json` in the current project folder. If the file is absent, the program starts with no registered students and creates it during registration. The sample project stores passwords as plain text for readability, so it is for classroom demonstration only and should not be used for real accounts.

## Major Functional Modules
1. Student Login
2. Quiz Management
3. Score Calculation

The remaining Python files are support, sample data, program startup, or simple test files, not extra end-user features.

## Documentation
See `statement.md` for the project scope and `PROJECT_REPORT.md` for requirements, diagrams, design decisions, implementation, testing, challenges, learnings, future enhancements, and references.

