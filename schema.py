from pydantic import BaseModel


# admin
class AdminBase(BaseModel):
    name: str
    email: str


class AdminCreate(AdminBase):
    password: str


class Admin(AdminBase):
    id: int

    class Config:
        orm_mode = True

#login_admin
class LoginAdmin(BaseModel):
    email: str
    password: str
class LoginAdminResponse(BaseModel):
    token: str

# setter
class SetterBase(BaseModel):
    name: str
    email: str


class SetterCreate(SetterBase):
    password: str


class Setter(SetterBase):
    id: int

    class Config:
        orm_mode = True

#login_setter
class LoginSetter(BaseModel):
    email: str
    password: str
class LoginSetterResponse(BaseModel):
    token: str

# solver
class SolverBase(BaseModel):
    name: str
    email: str


class SolverCreate(SolverBase):
    password: str


class Solver(SolverBase):
    id: int

    class Config:
        orm_mode = True

#login_solver
class LoginSolver(BaseModel):
    email: str
    password: str
class LoginSolverResponse(BaseModel):
    token: str