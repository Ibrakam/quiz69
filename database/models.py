"""
User
id
name
phone_number
level
reg_date

Question
id
qtext
v1
v2
v3
v4
level
correct_answer


UserAnswer
id
uid
answer
qid
correctness


Result
id
uid
correct_answers


"""
from sqlalchemy import (Integer, String, Boolean, 
                        DateTime, Column, ForeignKey)
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base



class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    phone_number = Column(String, unique=True, nullable=False)
    level = Column(String, default="easy")
    reg_date = Column(DateTime, default=datetime.now())


class Result(Base):
    __tablename__ = "results"
    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(Integer, ForeignKey("users.id"))
    correct_answers = Column(Integer, default=0)

    user_fk = relationship("User", lazy="subquery")


class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    qtext = Column(String, nullable=False)
    v1 = Column(String, nullable=False)
    v2 = Column(String, nullable=False)
    v3 = Column(String)
    v4 = Column(String)
    level = Column(String, default="easy")
    correct_answer = Column(String, nullable=False)


class UserAnswer(Base):
    __tablename__ = "useranswers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(Integer, ForeignKey("users.id"))
    answer = Column(String, nullable=False)
    qid = Column(Integer, ForeignKey("questions.id"))
    correctness = Column(Boolean, default=False)

    user_fk = relationship("User", lazy="subquery")
    question_fk = relationship("Question", lazy="subquery")



