from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import model, schema, crud
from database import engine, SessionLocal
from auth import create_token, decode_token
import logging

from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"login")
logging.basicConfig(level=logging.DEBUG)


model.Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# admin
@app.post("/signup/admins/", response_model=schema.Admin)
def create_admin(admin: schema.AdminCreate, db: Session = Depends(get_db)):
    db_admin = crud.get_admin_by_email(db, email=admin.email)
    if db_admin:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_admin(db=db, admin=admin)


# login
@app.post("/login/admins/", response_model=schema.LoginAdminResponse)
def login(login: schema.LoginAdmin, db: Session = Depends(get_db)):
    db_admins = crud.get_admin_by_email(db, email=login.email)
    if not db_admins:
        raise HTTPException(status_code=401, detail="username or password is incorrect")
    if db_admins.password != login.password:
        raise HTTPException(status_code=401, detail="username or password is incorrect")
    return {"token": create_token(db_admins.email)}


def get_current_admins(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
):
    token_payload = decode_token(token)
    email = token_payload["email"]
    admins = crud.get_admin_by_email(db, email)
    if admins:
        return admins
    raise HTTPException(status_code=401, detail="Unauthorized")


@app.get("/admins/", response_model=list[schema.Admin])
def read_admins(
    db: Session = Depends(get_db),
    current_admins: model.Admin = Depends(get_current_admins),
):
    logging.debug(f" {current_admins.name} is making the request")
    return crud.get_admins(db)


@app.get("/admins/{admin_id}", response_model=schema.Admin)
def read_admin(
    admin_id: int,
    db: Session = Depends(get_db),
    current_admins: model.Admin = Depends(get_current_admins),
):
    db_admin = crud.get_admin(db, admin_id=admin_id)
    logging.info(f" {current_admins.name} is making the request")
    if db_admin is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_admin


# setter
@app.post("/signup/setters/", response_model=schema.Setter)
def create_setter(setter: schema.SetterCreate, db: Session = Depends(get_db)):
    db_setter = crud.get_setter_by_email(db, email=setter.email)
    if db_setter:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_setter(db=db, setter=setter)


# login
@app.post("/login/setters/", response_model=schema.LoginSetterResponse)
def login(login: schema.LoginSetter, db: Session = Depends(get_db)):
    db_setters = crud.get_setter_by_email(db, email=login.email)
    if not db_setters:
        raise HTTPException(status_code=401, detail="username or password is incorrect")
    if db_setters.password != login.password:
        raise HTTPException(status_code=401, detail="username or password is incorrect")
    return {"token": create_token(db_setters.email)}


def get_current_setter(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
):
    token_payload = decode_token(token)
    email = token_payload["email"]
    setters = crud.get_setter_by_email(db, email)
    if setters:
        return setters
    raise HTTPException(status_code=401, detail="Unauthorized")


@app.get("/setters/", response_model=list[schema.Setter])
def read_setters(
    db: Session = Depends(get_db),
    current_setter: model.Setter = Depends(get_current_setter),
):
    logging.info(f" {current_setter.name} is making the request")
    return crud.get_setters(db)


@app.get("/setters/{setter_id}", response_model=schema.Setter)
def read_setter(
    setter_id: int,
    db: Session = Depends(get_db),
    current_setter: model.Setter = Depends(get_current_setter),
):
    db_setter = crud.get_setter(db, setter_id=setter_id)
    logging.info(f" {current_setter.name} is making the request")
    if db_setter is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_setter


# solver
@app.post("/signup/solvers/", response_model=schema.Solver)
def create_solver(solver: schema.SolverCreate, db: Session = Depends(get_db)):
    db_solver = crud.get_solver_by_email(db, email=solver.email)
    if db_solver:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_solver(db=db, solver=solver)


# login
@app.post("/login/solvers", response_model=schema.LoginSolverResponse)
def login(login: schema.LoginSolver, db: Session = Depends(get_db)):
    db_solver = crud.get_solver_by_email(db, email=login.email)
    if not db_solver:
        raise HTTPException(status_code=401, detail="username or password is incorrect")
    if db_solver.password != login.password:
        raise HTTPException(status_code=401, detail="username or password is incorrect")
    return {"token": create_token(db_solver.email)}


def get_current_solver(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
):
    token_payload = decode_token(token)
    email = token_payload["email"]
    solver = crud.get_solver_by_email(db, email)
    if solver:
        return solver
    raise HTTPException(status_code=401, detail="Unauthorized")


@app.get("/solvers/", response_model=list[schema.Solver])
def read_solvers(
    db: Session = Depends(get_db),
    current_solver: model.Solver = Depends(get_current_solver),
):
    logging.info(f" {current_solver.name} is making the request")
    return crud.get_solvers(db)


@app.get("/solvers/{solver_id}", response_model=schema.Solver)
def read_solver(
    solver_id: int,
    db: Session = Depends(get_db),
    current_solver: model.Solver = Depends(get_current_solver),
):
    db_solver = crud.get_solver(db, solver_id=solver_id)
    logging.info(f" {current_solver.name} is making the request")
    if db_solver is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_solver
