from fastapi import APIRouter
router = APIRouter()

#question
@router.post("/questions/", response_model=schema.Question)
def create_question(question: schema.QuestionCreate, db: Session = Depends(get_db), current_user: model.Question = Depends(get_current_user)):
    logging.info(f" {current_user.name} is making the request")
    return crud.create_question(db=db, question=question, author_id=current_user.id)

@router.get("/questions/", response_model=list[schema.QuestionRelation])
def read_questions(db: Session = Depends(get_db), current_user: model.Question = Depends(get_current_user)):
    logging.info(f" {current_user.name} is making the request")
    return crud.get_questions(db)

@router.get("/questions/{question_id}", response_model=schema.QuestionRelation)
def read_question(question_id: int, db: Session = Depends(get_db), current_user: model.Question = Depends(get_current_user),):
    db_question = crud.get_question_by_id(db, question_id=question_id)
    logging.info(f" {current_user.name} is making the request")
    if db_question is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_question