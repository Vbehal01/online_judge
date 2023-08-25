from fastapi import APIRouter
router = APIRouter()
from model.setter import Setter
from schema.user import User


# setter
@router.get("/setters/", response_model=list[User])
def read_setters(db: Session = Depends(get_db), current_user: Setter = Depends(get_current_user)):
    logging.info(f" {current_user.name} is making the request")
    return crud.get_setters(db)


@router.get("/setters/{setter_id}", response_model=User)
def read_setter(setter_id: int, db: Session = Depends(get_db), current_user: Setter = Depends(get_current_user)):
    db_setter = crud.get_setter(db, setter_id=setter_id)
    logging.info(f" {current_user.name} is making the request")
    if db_setter is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_setter