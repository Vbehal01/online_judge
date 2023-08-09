from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Admin(Base):
    __tablename__ = "admin"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String)
    email=Column(String)
    password=Column(String, nullable=False)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String)
    email=Column(String)
    password=Column(String, nullable=False)

class Quest(Base):
    __tablename__ = "quest"

    id = Column(Integer, primary_key=True, autoincrement=True)
    body=Column(String)

class Test_Case(Base):
    __tablename__ = "test_case"

    id = Column(Integer, primary_key=True, autoincrement=True)
    input=Column(String)
    output=Column(String)

class Tag(Base):
    __tablename__="tag"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String)

class Level(Base):
    __tablename__="level"

    id = Column(Integer, primary_key=True, autoincrement=True)
    level=Column(String)

class Sub(Base):
    __tablename__="sub"

    id = Column(Integer, primary_key=True, autoincrement=True)
    body=Column(String)

class Language(Base):
    __tablename__="language"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String)

class Questions(Quest):
    __tablename__="questions"

    user_admin_id=Column(Integer, ForeignKey(Admin.id))
    user_id=Column(Integer, ForeignKey(User.id))
    ques_tag=Column(Integer, ForeignKey(Tag.id))
    test_case=Column(Integer, ForeignKey(Test_Case.id))
    level=Column(Integer, ForeignKey(Level.id))
    Submission=Column(Integer, ForeignKey(Submission.id), default=0)

class TestCase(Test_Case):
    __tablename__="testcase"

    question_id=Column(Integer, ForeignKey(Quest.id))
    user_admin_id=Column(Integer, ForeignKey(Admin.id))

class Submission(Sub):
    __tablename__="submission"

    question_id=Column(Integer, ForeignKey(Quest.id))
    sub_lang=Column(Integer, ForeignKey(Language.id))

class User_Ques(Base):
    __tablename__="user_ques"

    user_id=Column(Integer, ForeignKey(User.id))
    ques_id=Column(Integer, ForeignKey(Questions.id))

class Ques_Tag(Base):
    __tablename__="ques_tag"
    ques_id=Column(Integer, ForeignKey(Questions.id))
    tag_id=Column(Integer, ForeignKey(Tag.id))

class Sub_Lang(Base):
    __tablename__="sub_lang"
    sub_id=Column(Integer, ForeignKey(Submission.id))
    lang_id=Column(Integer, ForeignKey(Language.id))