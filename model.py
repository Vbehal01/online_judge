from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Solver(Base):
    __tablename__ = "solvers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    password = Column(String, nullable=False)
    # submissions = relationship("Submission", back_populates="solvers", lazy="selectin")

class Setter(Base):
    __tablename__ = "setters"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    password = Column(String, nullable=False)
    # questions = relationship("Question", back_populates="setters", lazy="selectin")

class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    password = Column(String, nullable=False)


class Language(Base):
    __tablename__ = "languages"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
#     submissions = relationship("Submission", back_populates="languages", lazy="selectin")

# class Level(Base):
#     __tablename__ = "levels"

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     title = Column(String)
#     questions = relationship("Question", back_populates="levels", lazy="selectin")

# class Question(Base):
#     __tablename__ = "questions"

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     title = Column(String)
#     body = Column(String)
#     author_id = Column(Integer, ForeignKey(Setter.id))
#     level_id = Column(Integer, ForeignKey(Level.id))
#     setters = relationship("Setter", back_populates="questions", lazy="selectin")
#     levels = relationship("Level", back_populates="questions", lazy="selectin")
#     questions = relationship("Submission", back_populates="submissions", lazy="selectin")
#     tags = relationship("Tag", secondary="question_tag", back_populates="questions", lazy="selectin")
#     test_cases = relationship("TestCase", back_populates="questions", lazy="selectin")

# class Tag(Base):
#     __tablename__ = "tags"

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     title = Column(String)
#     questions = relationship("Questions",secondary="question_tag",back_populates="question_tags",lazy="selectin")

# class QuestionTag(Base):
#     __tablename__ = "question_tag"

#     question_id = Column(Integer, ForeignKey(Question.id), primary_key=True)
#     tag_id = Column(Integer, ForeignKey(Tag.id), primary_key=True)

# class TestCase(Base):
#     __tablename__ = "test_cases"

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     input = Column(String)
#     output = Column(String)
#     question_id = Column(Integer, ForeignKey(Question.id))
#     questions = relationship("Question", back_populates="test_cases", lazy="selectin")

# class Submission(Base):
#     __tablename__ = "submissions"

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     body = Column(String)
#     solver_id = Column(Integer, ForeignKey(Solver.id))
#     language_id = Column(Integer, ForeignKey(Language.id))
#     failed_test_case_id = Column(Integer, ForeignKey(TestCase.id))
#     question_id = Column(Integer, ForeignKey(Question.id))
#     solvers = relationship("Solver", back_populates="submissions", lazy="selectin")
#     languages = relationship("Language", back_populates="submissions", lazy="selectin")
#     submissions = relationship("Question", back_populates="questions", lazy="selectin")