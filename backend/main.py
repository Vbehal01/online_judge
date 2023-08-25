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
        raise HTTPException(status_code=400, detail="role must be Admin, Setter, Solver")


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
@app.get("/setters/", response_model=list[schema.SetterRelation])
def read_setters(db: Session = Depends(get_db), current_user: model.Setter = Depends(get_current_user)):
    logging.info(f" {current_user.name} is making the request")
    return crud.get_setters(db)


@app.get("/setters/{setter_id}", response_model=schema.SetterRelation)
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
def create_langauge(language: schema.LanguageCreate, db: Session = Depends(get_db), current_user: model.Language = Depends(get_current_user)):
    logging.info(f" {current_user.name} is making the request")
    return crud.create_language(db=db, language=language)

@app.get("/languages/", response_model=list[schema.Language])
def read_languages(db: Session = Depends(get_db), current_user: model.Language = Depends(get_current_user)):
    logging.info(f" {current_user.name} is making the request")
    return crud.get_languages(db)

@app.get("/languages/{language_id}", response_model=schema.Language)
def read_language(language_id: int, db: Session = Depends(get_db), current_user: model.Language = Depends(get_current_user),):
    db_language = crud.get_language_by_id(db, language_id=language_id)
    logging.info(f" {current_user.name} is making the request")
    if db_language is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_language


#level
@app.post("/levels/", response_model=schema.Level)
def create_level(level: schema.LevelCreate, db: Session = Depends(get_db), current_user: model.Level = Depends(get_current_user)):
    logging.info(f" {current_user.name} is making the request")
    return crud.create_level(db=db, level=level)

@app.get("/levels/", response_model=list[schema.LevelRelation])
def read_levels(db: Session = Depends(get_db), current_user: model.Level = Depends(get_current_user)):
    logging.info(f" {current_user.name} is making the request")
    return crud.get_levels(db)

@app.get("/levels/{level_id}", response_model=schema.LevelRelation)
def read_level(level_id: int, db: Session = Depends(get_db), current_user: model.Level = Depends(get_current_user),):
    db_level = crud.get_level_by_id(db, level_id=level_id)
    logging.info(f" {current_user.name} is making the request")
    if db_level is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_level


#question
@app.post("/questions/", response_model=schema.Question)
def create_question(question: schema.QuestionCreate, db: Session = Depends(get_db), current_user: model.Question = Depends(get_current_user)):
    logging.info(f" {current_user.name} is making the request")
    return crud.create_question(db=db, question=question, author_id=current_user.id)

@app.get("/questions/", response_model=list[schema.QuestionRelation])
def read_questions(db: Session = Depends(get_db), current_user: model.Question = Depends(get_current_user)):
    logging.info(f" {current_user.name} is making the request")
    return crud.get_questions(db)

@app.get("/questions/{question_id}", response_model=schema.QuestionRelation)
def read_question(question_id: int, db: Session = Depends(get_db), current_user: model.Question = Depends(get_current_user),):
    db_question = crud.get_question_by_id(db, question_id=question_id)
    logging.info(f" {current_user.name} is making the request")
    if db_question is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_question


#tag
@app.post("/tags/", response_model=schema.Tag)
def create_tag(tag: schema.TagCreate, db: Session = Depends(get_db), current_user: model.Tag = Depends(get_current_user)):
    logging.info(f" {current_user.name} is making the request")
    return crud.create_tag(db=db, tag=tag)

@app.get("/tags/", response_model=list[schema.TagRelation])
def read_tags(db: Session = Depends(get_db), current_user: model.Tag = Depends(get_current_user)):
    logging.info(f" {current_user.name} is making the request")
    return crud.get_tags(db)

@app.get("/tags/{tag_id}", response_model=schema.TagRelation)
def read_tag(tag_id: int, db: Session = Depends(get_db), current_user: model.Tag = Depends(get_current_user),):
    db_tag = crud.get_tag_by_id(db, tag_id=tag_id)
    logging.info(f" {current_user.name} is making the request")
    if db_tag is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_tag


#questiontag
@app.post("/tags/question/{question_id}", response_model=schema.QuestionTag)
def create_question_tag(question_id: int, question_tag: schema.QuestionTagCreate, db: Session = Depends(get_db), current_user: model.QuestionTag = Depends(get_current_user)):
    logging.info(f" {current_user.name} is making the request")
    return crud.create_question_tag(db=db, question_tag=question_tag, question_id=question_id)


#testcase
@app.post("/questions/{question_id}/testcases", response_model=schema.TestCase)
def create_testcase(question_id: int, testcase: schema.TestCaseCreate, db: Session = Depends(get_db), current_user: model.TestCase = Depends(get_current_user)):
    logging.info(f" {current_user.name} is making the request")
    return crud.create_testcase(db=db, testcase=testcase, question_id=question_id)

@app.get("/testcases/", response_model=list[schema.TestCaseRelation])
def read_testcases(db: Session = Depends(get_db), current_user: model.TestCase = Depends(get_current_user)):
    logging.info(f" {current_user.name} is making the request")
    return crud.get_testcases(db)

@app.get("/testcases/{test_case_id}", response_model=schema.TestCaseRelation)
def read_testcase(test_case_id: int, db: Session = Depends(get_db), current_user: model.TestCase = Depends(get_current_user),):
    db_test_case = crud.get_test_case_by_id(db, test_case_id=test_case_id)
    logging.info(f" {current_user.name} is making the request")
    if db_test_case is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_test_case


#submission
@app.post("/submissions", response_model=schema.Submission)
def create_submission(submission: schema.SubmissionCreate, db: Session = Depends(get_db), current_user: model.Submission = Depends(get_current_user)):
    logging.info(f" {current_user.name} is making the request")
    db_submission = crud.create_submission(db=db, submission=submission, solver_id=current_user.id)
    return db_submission
