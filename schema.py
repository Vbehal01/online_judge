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

class LangaugeCreate(LanguageBase):
    pass

class Language(LanguageBase):
    id: int
    
    class Config:
        orm_mode = True
