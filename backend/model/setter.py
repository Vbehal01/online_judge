from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Setter(Base):
    __tablename__ = "setters"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    password = Column(String, nullable=False)
    questions = relationship("Question", back_populates="setter", lazy="selectin")