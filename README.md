# 🧑‍🏫 Coach & Student Management System

This project demonstrates a simple multi-class system in Python, built with clean Object-Oriented Programming (OOP) principles and comprehensive testing. It is structured for learners to practice class design, composition, and testing strategies.

## 🚀 Learning Objectives

## 📂 Project Structure
```bash
.
├── lib/
│   ├── coach.py        # Contains the Coach class
│   └── student.py      # Contains the Student class
└── tests/
    ├── test_coach_integration.py   # Tests the interaction between Student and Coach classes
    └── test_coach_unit.py    # Tests the Coach class in isolation
```
---

## Project Diagram



## 💻 How to Run the Code

To explore the classes and their methods, you can use the Python interactive shell (REPL) directly from your terminal.

First, navigate to the root of the project directory.

### Step 1: Testing the `Student` Class (Isolation)

The `Student` class is responsible for managing its own name and submissions.

1.  Start the Python shell:

    ```bash
    python # or python3
    ```

2.  Import the class and create an instance:

    ```python
    >>> from lib.student import Student
    >>> student = Student("Asha")
    >>> student.name
    'Asha'
    >>> student.submissions
    []
    ```

3.  Test the core functionality:

    ```python
    >>> student.add_submission("challenge-01-oop")
    >>> student.add_submission("challenge-02-testing")
    >>> student.submissions
    ['challenge-01-oop', 'challenge-02-testing']
    >>> student.count_submissions()
    2
    ```

## 🧪 Running the Tests

The project uses `pytest` for running automated tests.

1.  Run all tests from the project root:

    ```bash
    pytest -xv
    ```
