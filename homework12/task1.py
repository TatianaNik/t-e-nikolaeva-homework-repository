import datetime

from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine = create_engine("sqlite+pysqlite:///main.db")
Session = sessionmaker(bind=engine)
session = Session()


class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column('first_name', String)
    last_name = Column('last_name', String)


class Teacher(Person):
    __tablename__ = 'teachers'
    id = Column(Integer, ForeignKey("persons.id"), primary_key=True, autoincrement=True)
    homework_done = Column('homework_done', String)


class Student(Person):
    __tablename__ = 'students'
    id = Column(Integer, ForeignKey("persons.id"), primary_key=True, autoincrement=True)

    def do_homework(self, homework, solution):
        if homework.is_active():
            homework_result = HomeworkResult(student_id=self.id, solution=solution)
            session.add(homework_result)
            return homework_result
        else:
            raise DeadlineError("You are late")


class Homework(Base):
    __tablename__ = 'homework'
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column('text', String)
    deadline = Column('deadline', Integer)
    created = Column('created', DateTime)

    def is_active(self):
        return datetime.timedelta(days=self.deadline) + self.created >= datetime.datetime.now()


class HomeworkResult(Base):
    __tablename__ = 'homeworkresult'
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    solution = Column('solution', String)

    def __str__(self):
        return f'{self.id} - {self.solution} :: {self.student_id}'


if __name__ == '__main__':

    student = Student(first_name="Alex", last_name="Ivanov")
    hw = Homework(text='1', deadline=5, created=datetime.datetime.now())
    session.add(student)
    session.add(hw)
    session.commit()
    student.do_homework(hw, 'test')
    session.commit()
    res = session.query(HomeworkResult).all()
    [print(x) for x in res]


