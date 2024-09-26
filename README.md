QuizAnswerChecker
Description

QuizAnswerChecker is a Python-based solution designed to evaluate student quiz answers by comparing them to a predefined answer key. The program reads the student's answers from a file, counts the correct and incorrect responses, and determines whether the student passed or failed based on a customizable passing threshold. This tool is ideal for educators or anyone who needs to automate the grading of multiple-choice quizzes.
Features

    Reads student answers from an external text file (students.txt).
    Compares student answers against a predefined correct answer list.
    Calculates the total number of correct and incorrect answers.
    Identifies the specific question numbers that were answered incorrectly.
    Provides a pass/fail outcome based on a customizable passing score threshold (default: 15 out of 20).
    Clean, simple output detailing performance metrics.

Requirements

    Python 3.x

Installation

    Clone the repository:

    bash

git clone https://github.com/yourusername/QuizAnswerChecker.git
cd QuizAnswerChecker

Ensure Python 3.x is installed:

    You can download Python here.

Create a text file (students.txt):

    Each line of the file should contain a student's answer (A, B, C, or D).
    Example format:

    css

        A
        C
        A
        B
        ...

Usage

    Place the students.txt file in the same directory as the Python script.

    Run the program:

    bash

    python quiz_answer_checker.py

    The program will output the student's results:
        Pass/Fail Status based on the number of correct answers.
        Total Number Correct and Total Number Incorrect.
        A list of Incorrect Question Numbers for review.

Example Output

bash

You passed!
Total Number Correct: 16
Total Number Incorrect: 4
Incorrect question numbers: [2, 6, 12, 18]

Customization

    You can modify the correct answers by editing the predefined list in the script:

    python

answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']

To change the passing threshold, modify the comparison condition in the code:

python

    if correct >= 15:
        print("You passed!")

Future Enhancements

    Adding support for multiple students in one file.
    Implementing a graphical user interface (GUI) for easier interaction.
    Creating a more robust file format for student answers, such as CSV.
