import sqlalchemy
import alembic
from datetime import datetime

from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, relationship
from homework12.task1 import Person, Teacher, Student, Homework, HomeworkResult

engine = create_engine("sqlite+pysqlite:///main.db")
Session = sessionmaker(bind=engine)
session = Session()

person1 = Person(id=1, first_name="Ivan", last_name="Ivanov")
person2 = Person(id=2, first_name="Petr", last_name="Petrov")
person3 = Person(id=3, first_name="Alex", last_name="Alexeev")
person4 = Person(id=4, first_name="Mike", last_name="Mikin")

# student1 = Student(id=1)
# student2 = Student(id=2)
#
# teacher1 = Teacher(id=3, homework_done='homework_done1???')
# teacher2 = Teacher(id=4, homework_done='homework_done2???')
#
# homework1 = Homework(id=1, text="Python", deadline=5, created=datetime.now())
# homework2 = Homework(id=2, text="SQL", deadline=2, created=datetime.now())
#
# homework_result1 = HomeworkResult(id=1, student_id=1, solution="solution1")
# homework_result2 = HomeworkResult(id=2, student_id=2, solution="solution2")
#
# session.add_all([person1, person2, person3, person4, student1, student2,
#                  teacher1, teacher2, homework1, homework2, homework_result1, homework_result2])

session.add(person1)
session.commit()


