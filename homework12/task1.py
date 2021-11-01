import sqlalchemy
import datetime
from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# engine = create_engine("sqlite+pysqlite:///main.db")
# Session = sessionmaker(bind=engine)
# session = Session()


class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)
    first_name = Column('first_name', String)
    last_name = Column('last_name', String)

# person = Person("Alex", "Ivanov")
# session.add(person)
# def datainit : создаем записи
# def execute:  читать данные из базы
# def удалить все записи из базы
# if name = main:  по очереди вызывать 3 функции

class Teacher(Person):
    __tablename__ = 'teachers'
    id = Column(Integer, ForeignKey("persons.id"), primary_key=True)
    homework_done = Column('homework_done', String) # many to many


class Student(Person):
    __tablename__ = 'students'
    id = Column(Integer, ForeignKey("persons.id"), primary_key=True)
    def do_homework(self, homework, solution):
        if homework.is_active():

            return HomeworkResult(self, homework, solution)  # потом записать в базу рез
        else:
            raise DeadlineError("You are late")

class Homework(Base):
    __tablename__ = 'homework'
    id = Column(Integer, primary_key=True)
    text = Column('text', String)
    deadline = Column('deadline', Integer)
    created = Column('created', DateTime)
    def is_active(self):
        return self.deadline + self.created >= datetime.datetime.now()


class HomeworkResult(Base):
    __tablename__ = 'homeworkresult'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    solution = Column('solution', String)


