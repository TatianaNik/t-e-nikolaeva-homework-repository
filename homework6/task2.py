"""

Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную
1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)
HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'
    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания
2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.
3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования
4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.
    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.

"""
import datetime
from collections import defaultdict


class Homework:
    def __init__(self, text, deadline, created):
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = created

    def is_active(self):
        return self.deadline + self.created >= datetime.datetime.now()


class DeadlineError(Exception):
    pass


class Person:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name


class Student(Person):
    def do_homework(self, homework, solution):
        if homework.is_active():
            return HomeworkResult(self, homework, solution)
        else:
            raise DeadlineError("You are late")


class HomeworkResult:
    def __init__(self, author, homework, solution):
        self.author = author
        self.solution = solution

        if isinstance(homework, Homework):
            self.homework = homework
        else:
            raise AttributeError('You gave not a Homework object')


class Teacher(Person):
    homework_done = defaultdict()

    @staticmethod
    def create_homework(text, deadline):
        created = datetime.datetime.now()
        homework = Homework(text, deadline, created)
        return homework

    def check_homework(self, homeworkresult):

        if len(homeworkresult.solution) > 5:
            self.__class__.homework_done[homeworkresult.homework] = homeworkresult.solution
            return True
        else:
            return False

    @classmethod
    def reset_results(cls, homework=None):
        if type(homework) == Homework:
            cls.homework_done[homework] = None
        elif homework is None:
            cls.homework_done = defaultdict()
        else:
            raise TypeError("must be Homework or None")


if __name__ == '__main__':
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    print("result_1: ", result_1)
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    print("result_2: ", result_2)
    result_3 = lazy_student.do_homework(docs_hw, 'done')
    print("result_3: ", result_3)
    print(HomeworkResult(good_student, "fff", "Solution"))
    # try:
    #     result_4 = HomeworkResult(good_student, "fff", "Solution")
    # except Exception:
    #     print('There was an exception here')

    p = opp_teacher.check_homework(result_1)
    print("p: ", p)
    temp_1 = opp_teacher.homework_done
    print("temp_1: ", temp_1)

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    print('temp_2: ', temp_2)
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print("Teacher.homework_done[oop_hw]", Teacher.homework_done[oop_hw])
    Teacher.reset_results()
