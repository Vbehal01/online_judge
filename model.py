from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Solver(Base):
    __tablename__ = "solvers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String)
    email=Column(String)
    password=Column(String, nullable=False)

    solver_submissions=relationship("Submission" , back_populates="submission_solvers", lazy="selectin")


class Setter(Base):
    __tablename__ = "setters"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String)
    email=Column(String)
    password=Column(String, nullable=False)

    setter_questions=relationship("Question" , back_populates="question_setters", lazy="selectin")


class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String)
    email=Column(String)
    password=Column(String, nullable=False)


class Language(Base):
    __tablename__ = "languages"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title=Column(String)

    language_submissions=relationship("Submission" , back_populates="submission_languages", lazy="selectin")


class Level(Base):
    __tablename__ = "levels"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title=Column(String)

    level_questions=relationship("Question" , back_populates="question_levels", lazy="selectin")


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title=Column(String)
    body=Column(String)
    author_id=Column(Integer, ForeignKey(Setter.id))
    level_id=Column(Integer, ForeignKey(Level.id))

    question_setters=relationship("Setter" , back_populates="setter_questions", lazy="selectin")
    question_levels=relationship("Level" , back_populates="level_questions", lazy="selectin")
    question_submissions=relationship("Submission" , back_populates="submission_questions", lazy="selectin")
    question_tags=relationship("Tag" ,secondary="question_tag", back_populates="tag_questions", lazy="selectin")
    question_test_cases=relationship("TestCase" , back_populates="test_case_questions", lazy="selectin")


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title=Column(String)

    tag_questions=relationship("Questions" ,secondary="question_tag", back_populates="question_tags", lazy="selectin")


class QuestionTag(Base):
    __tablename__ = "question_tag"

    question_id = Column(Integer, ForeignKey(Question.id))
    tag_id=Column(Integer, ForeignKey(Tag.id))


class TestCase(Base):
    __tablename__ = "test_cases"

    id = Column(Integer, primary_key=True, autoincrement=True)
    input=Column(String)
    output=Column(String)
    question_id=Column(Integer, ForeignKey(Question.id))

    test_case_questions=relationship("Question" , back_populates="question_test_cases", lazy="selectin")


class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    body=Column(String)
    solver_id=Column(Integer, ForeignKey(Solver.id))
    language_id=Column(Integer, ForeignKey(Language.id))
    failed_test_case_id=Column(Integer, ForeignKey(TestCase.id))
    question_id=Column(Integer, ForeignKey(Question.id))

    submission_solvers=relationship("Solver" , back_populates="solver_submissions", lazy="selectin")
    submission_languages=relationship("Language" , back_populates="language_submissions", lazy="selectin")
    submission_questions=relationship("Question" , back_populates="question_submissions", lazy="selectin")