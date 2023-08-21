from sqlalchemy.orm import Session
import model, schema


# admin
def get_admin(db: Session, admin_id: int):
    return db.query(model.Admin).filter(model.Admin.id == admin_id).first()


def get_admin_by_email(db: Session, email: str):
    return db.query(model.Admin).filter(model.Admin.email == email).first()


def get_admins(db: Session):
    return db.query(model.Admin).all()


def create_admin(db: Session, admin: schema.UserCreate):
    db_admin = model.Admin(name=admin.name, email=admin.email, password=admin.password)
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin


# setter
def get_setter(db: Session, setter_id: int):
    return db.query(model.Setter).filter(model.Setter.id == setter_id).first()


def get_setter_by_email(db: Session, email: str):
    return db.query(model.Setter).filter(model.Setter.email == email).first()


def get_setters(db: Session):
    return db.query(model.Setter).all()


def create_setter(db: Session, setter: schema.UserCreate):
    db_setter = model.Setter(
        name=setter.name, email=setter.email, password=setter.password
    )
    db.add(db_setter)
    db.commit()
    db.refresh(db_setter)
    return db_setter


# solver
def get_solver(db: Session, solver_id: int):
    return db.query(model.Solver).filter(model.Solver.id == solver_id).first()


def get_solver_by_email(db: Session, email: str):
    return db.query(model.Solver).filter(model.Solver.email == email).first()


def get_solvers(db: Session):
    return db.query(model.Solver).all()


def create_solver(db: Session, solver: schema.UserCreate):
    db_solver = model.Solver(name=solver.name, email=solver.email, password=solver.password)
    db.add(db_solver)
    db.commit()
    db.refresh(db_solver)
    return db_solver


#language
def create_language(db: Session, language: schema.LanguageCreate):
    db_language = model.Language(title=language.title)
    db.add(db_language)
    db.commit()
    db.refresh(db_language)
    return db_language

def get_language_by_id(db: Session, language_id: int):
    return db.query(model.Language).filter(model.Language.id == language_id).first()


def get_languages(db: Session):
    return db.query(model.Language).all()

#level
def create_level(db: Session, level: schema.LevelCreate):
    db_level = model.Level(title=level.title)
    db.add(db_level)
    db.commit()
    db.refresh(db_level)
    return db_level

def get_level_by_id(db: Session, level_id: int):
    return db.query(model.Level).filter(model.Level.id == level_id).first()


def get_levels(db: Session):
    return db.query(model.Level).all()


#question
def get_question_by_id(db: Session, question_id: int):
    return db.query(model.Question).filter(model.Question.id == question_id).first()


def get_questions(db: Session):
    return db.query(model.Question).all()


def create_question(db: Session, question: schema.QuestionCreate, author_id: str):
    db_question = model.Question(body=question.body, level_id=question.level_id, title=question.title, author_id=author_id)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question


#tag
def create_tag(db: Session, tag: schema.TagCreate):
    db_tag = model.Tag(title=tag.title)
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag

def get_tag_by_id(db: Session, tag_id: int):
    return db.query(model.Tag).filter(model.Tag.id == tag_id).first()


def get_tags(db: Session):
    return db.query(model.Tag).all()


#question_tag
def create_question_tag(db: Session, question_tag: schema.QuestionTagCreate, question_id: int):
    db_question_tag = model.QuestionTag(tag_id=question_tag.tag_id, question_id=question_id)
    db.add(db_question_tag)
    db.commit()
    db.refresh(db_question_tag)
    return db_question_tag
