from pydantic import BaseModel


# user
class UserBase(BaseModel):
    name: str
    email: str


class UserCreateSign(UserBase):
    role: str
    password: str

class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


# login_user
class Login(BaseModel):
    role: str
    email: str
    password: str


class LoginResponse(BaseModel):
    token: str


#language
class LanguageBase(BaseModel):
    title: str

class LanguageCreate(LanguageBase):
    pass

class Language(LanguageBase):
    id: int
    
    class Config:
        orm_mode = True


#level
class LevelBase(BaseModel):
    title: str

class LevelCreate(LevelBase):
    pass

class Level(LevelBase):
    id: int
    
    class Config:
        orm_mode = True


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


#tag
class TagBase(BaseModel):
    title: str

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    id: int
    
    class Config:
        orm_mode = True


#questiontag
class QuestionTagBase(BaseModel):
    tag_id: int

class QuestionTagCreate(QuestionTagBase):
    pass

class QuestionTag(QuestionTagBase):
    question_id: int
    
    class Config:
        orm_mode = True


#relations
class SetterRelation(User):
    questions: list[Question]

class QuestionRelation(Question):
    setter: User
    level: Level
    tags: list[Tag]

class LevelRelation(Level):
    questions: list[Question]

class TagRelation(Tag):
    questions: list[Question]
