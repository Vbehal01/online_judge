from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    body = Column(String)
    author_id = Column(Integer, ForeignKey(Setter.id))
    level_id = Column(Integer, ForeignKey(Level.id))
    setter = relationship("Setter", back_populates="questions", lazy="selectin")
    level = relationship("Level", back_populates="questions", lazy="selectin")
#     questions = relationship("Submission", back_populates="submissions", lazy="selectin")
    tags = relationship("Tag", secondary="question_tag", back_populates="questions", lazy="selectin")
    test_cases = relationship("TestCase", back_populates="questions", lazy="selectin")
