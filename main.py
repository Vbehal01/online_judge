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


# signup
@app.post("/signup/", response_model=schema.User)
def create_user(user: schema.UserCreateSign, db: Session = Depends(get_db)):
    if user.role == "Admin":
        db_user = crud.get_admin_by_email(db, email=user.email)
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        return crud.create_admin(db=db, admin=user)

    elif user.role == "Setter":
        db_user = crud.get_setter_by_email(db, email=user.email)
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        return crud.create_setter(db=db, setter=user)

    elif user.role == "Solver":
        db_user = crud.get_solver_by_email(db, email=user.email)
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        return crud.create_solver(db=db, solver=user)

    else:
        raise HTTPException(status_code=400, detail="role must be admin, setter, solver")


#login
@app.post("/login/", response_model=schema.LoginResponse)
def login(user: schema.Login, db: Session = Depends(get_db)):
    if user.role == "Admin":
        db_user = crud.get_admin_by_email(db, email=user.email)
        if not db_user:
            raise HTTPException(status_code=401, detail="username or password is incorrect")
        if db_user.password != user.password:
            raise HTTPException(status_code=401, detail="username or password is incorrect")
        return {"token": create_token(db_user.email, user.role)}
    
    elif user.role == "Solver":
        db_user = crud.get_solver_by_email(db, email=user.email)
        if not db_user:
            raise HTTPException(status_code=401, detail="username or password is incorrect")
        if db_user.password != user.password:
            raise HTTPException(status_code=401, detail="username or password is incorrect")
        return {"token": create_token(db_user.email, user.role)}
    
    elif user.role == "Setter":
        db_user = crud.get_setter_by_email(db, email=user.email)
        if not db_user:
            raise HTTPException(status_code=401, detail="username or password is incorrect")
        if db_user.password != user.password:
            raise HTTPException(status_code=401, detail="username or password is incorrect")
        return {"token": create_token(db_user.email, user.role)}
    
    else:
        raise HTTPException(status_code=400, detail="role must be admin, setter, solver")


def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    token_payload = decode_token(token)
    email = token_payload["email"]
    role = token_payload["role"]
    if role == "Admin":
        user = crud.get_admin_by_email(db, email)
        if user:
            return user
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    elif role == "Setter":
        user = crud.get_setter_by_email(db, email)
        if user:
            return user
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    elif role == "Solver":
        user = crud.get_solver_by_email(db, email)
        if user:
            return user
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    else:
        raise HTTPException(status_code=400, detail="role must be admin, setter, solver")





# admin
@app.get("/admins/", response_model=list[schema.User])
def read_Users(db: Session = Depends(get_db), current_user: model.Admin = Depends(get_current_user)):
    logging.debug(f" {current_user.name} is making the request")
    return crud.get_admins(db)


@app.get("/admins/{admin_id}", response_model=schema.User)
def read_admin(admin_id: int, db: Session = Depends(get_db), current_user: model.Admin = Depends(get_current_user)):
    db_admin = crud.get_admin(db, admin_id=admin_id)
    logging.info(f" {current_user.name} is making the request")
    if db_admin is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_admin


# setter
@app.get("/setters/", response_model=list[schema.User])
def read_setters(db: Session = Depends(get_db), current_user: model.Setter = Depends(get_current_user)):
    logging.info(f" {current_user.name} is making the request")
    return crud.get_setters(db)


@app.get("/setters/{setter_id}", response_model=schema.User)
def read_setter(setter_id: int, db: Session = Depends(get_db), current_user: model.Setter = Depends(get_current_user)):
    db_setter = crud.get_setter(db, setter_id=setter_id)
    logging.info(f" {current_user.name} is making the request")
    if db_setter is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_setter


# solver
@app.get("/solvers/", response_model=list[schema.User])
def read_solvers(db: Session = Depends(get_db), current_user: model.Solver = Depends(get_current_user)):
    logging.info(f" {current_user.name} is making the request")
    return crud.get_solvers(db)


@app.get("/solvers/{solver_id}", response_model=schema.User)
def read_solver(solver_id: int, db: Session = Depends(get_db), current_user: model.Solver = Depends(get_current_user),):
    db_solver = crud.get_solver(db, solver_id=solver_id)
    logging.info(f" {current_user.name} is making the request")
    if db_solver is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_solver


#language
@app.post("/languages/", response_model=schema.Language)
def create_langauge(language: schema.LangaugeCreate, db: Session = Depends(get_db), current_user: model.Language = Depends(get_current_user)):
    logging.info(f" {current_user.name} is making the request")
    user= crud.create_language(db=db, langauge=language)
    print(user.__dict__)
    return user
