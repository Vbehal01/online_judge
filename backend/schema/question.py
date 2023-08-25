from pydantic import BaseModel
#question
class QuestionBase(BaseModel):
    title: str
    body: str
    level_id: int

class QuestionCreate(QuestionBase):
    pass

class Question(QuestionBase):
    id: int
    author_id: int
    
    class Config:
        orm_mode = True