from lib.coach import Coach
from unittest.mock import Mock

def test_count_submissions_where_multiple_students_have_multiple_submissions():
    claire = Coach("Claire")
    lea = Mock()
    ginger = Mock()

    claire.add_student(lea)
    claire.add_student(ginger)
    
    lea.count_submissions.return_value = 3
    ginger.count_submissions.return_value = 2

    assert claire.count_submissions() == 5