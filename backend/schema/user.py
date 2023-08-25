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
