from fastapi import Depends
from fastapi import FastAPI
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database import Base
from app.database import SessionLocal
from app.database import engine

from app import crud
from app.schemas import FeedbackCreate
from app.schemas import FeedbackResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@app.post("/feedback", response_model=FeedbackResponse)
def create_feedback(feedback: FeedbackCreate, db: Session = Depends(get_db)):
    return crud.create_feedback(db, feedback)


@app.get("/feedback/{feedback_id}",response_model=FeedbackResponse)
def get_feedback(feedback_id: int, db: Session = Depends(get_db)):
    feedback = crud.get_feedback(db, feedback_id)

    if not feedback:
        raise HTTPException(status_code=404, detail="Feedback not found")

    return feedback


@app.get("/feedbacks", response_model=list[FeedbackResponse])
def list_feedbacks(db: Session = Depends(get_db)):
    return crud.get_all_feedbacks(db)


@app.delete("/feedback/{feedback_id}")
def delete_feedback(feedback_id: int, db: Session = Depends(get_db)):
    feedback = crud.delete_feedback(db,feedback_id)

    if not feedback:
        raise HTTPException(status_code=404, detail="Feedback not found")

    return {
        "message": "Feedback deleted successfully"
    }