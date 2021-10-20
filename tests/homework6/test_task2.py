from homework6.task2 import Homework, DeadlineError, Person, Student, HomeworkResult, Teacher
import pytest
import datetime
from collections import defaultdict

# def test_check_homework_is_active():
#     homework1 = Homework('homework1.txt', 5, datetime.datetime.now())
#     assert(Homework.is_active(homework1) == True)
#
#
# def test_create_homework_do_homework_check_homework_and_homework_done_good_student():
#     math_teacher = Teacher('Petrov', 'Petr')
#     good_student = Student('Good', 'Nikolay')
#     math_hw = math_teacher.create_homework('arithmetics', 5)
#     result_1 = good_student.do_homework(math_hw, 'I have done this hw')
#     assert(math_teacher.check_homework(result_1) == True)
#     assert(Teacher.homework_done[math_hw] == 'I have done this hw')
#
#
# def test_create_homework_do_homework_check_homework_and_homework_done_bad_student():
#     math_teacher = Teacher('Petrov', 'Petr')
#     bad_student = Student('Ivanov', 'Ivan')
#     math_hw1 = math_teacher.create_homework('division', 1)
#     result_2 = bad_student.do_homework(math_hw1, 'Done')
#     assert(math_teacher.check_homework(result_2) == False)



# def test_homework_result_with_not_homework_object():
#     good_student = Student('Good', 'Nikolay')
#     res = HomeworkResult(good_student, 'not_homework', 'solution')
#     assert(res == AttributeError)




with pytest.raises(AttributeError, match='You gave not a Homework object'):
    good_student = Student('Good', 'Nikolay')
    result = HomeworkResult(good_student, 'not_homework', 'solution')
    raise AttributeError('You gave not a Homework object')
