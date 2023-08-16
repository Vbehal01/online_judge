from sqlalchemy.orm import Session, joinedload
from sqlalchemy import update
from fastapi import HTTPException
import model, schema


# admin
def get_admin(db: Session, admin_id: int):
    return db.query(model.Admin).filter(model.Admin.id == admin_id).first()


def get_admin_by_email(db: Session, email: str):
    return db.query(model.Admin).filter(model.Admin.email == email).first()


def get_admins(db: Session):
    return db.query(model.Admin).all()


def create_admin(db: Session, admin: schema.AdminCreate):
    db_admin = model.Admin(name=admin.name, email=admin.email, password=admin.password)
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin

#setter
def get_setter(db: Session, setter_id: int):
    return db.query(model.Setter).filter(model.Setter.id == setter_id).first()


def get_setter_by_email(db: Session, email: str):
    return db.query(model.Setter).filter(model.Setter.email == email).first()


def get_setters(db: Session):
    return db.query(model.Setter).all()


def create_setter(db: Session, setter: schema.SetterCreate):
    db_setter = model.Setter(name=setter.name, email=setter.email, password=setter.password)
    db.add(db_setter)
    db.commit()
    db.refresh(db_setter)
    return db_setter

#solver
def get_solver(db: Session, solver_id: int):
    return db.query(model.Solver).filter(model.Solver.id == solver_id).first()


def get_solver_by_email(db: Session, email: str):
    return db.query(model.Solver).filter(model.Solver.email == email).first()


def get_solvers(db: Session):
    return db.query(model.Solver).all()


def create_solver(db: Session, solver: schema.SolverCreate):
    db_solver = model.Solver(name=solver.name, email=solver.email, password=solver.password)
    db.add(db_solver)
    db.commit()
    db.refresh(db_solver)
    return db_solver