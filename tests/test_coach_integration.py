from lib.coach import Coach
from lib.student import Student


#Make use of the count_submissions method from the student class 
#to count all the submissions of all the students.

def test_count_submissions_where_student_has_no_submissions():
    #Create a coach
    #Create a student
    #Give student to the coach
    #Count the submissions

    claire = Coach("Claire")
    lea = Student("Lea")

    claire.add_student(lea)

    assert claire.count_submissions() == 0

def test_count_submissions_where_student_has_one_submission():
    claire = Coach("Claire")
    lea = Student("Lea")

    claire.add_student(lea)
    lea.add_submission("This is a great submission")

    assert claire.count_submissions() == 1


def test_count_submissions_where_multiple_students_have_multiple_submissions():
    claire = Coach("Claire")
    lea = Student("Lea")
    ginger = Student("Ginger")

    claire.add_student(lea)
    claire.add_student(ginger)
    lea.add_submission("This is a great submission")
    ginger.add_submission("This is a great submission")

    assert claire.count_submissions() == 2