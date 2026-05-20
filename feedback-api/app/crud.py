from sqlalchemy.orm import Session

from app.models import Feedback
from app.schemas import FeedbackCreate


def create_feedback(db: Session, feedback: FeedbackCreate):
    db_feedback = Feedback(
        user_name=feedback.user_name,
        email=feedback.email,
        message=feedback.message
    )

    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)

    return db_feedback


def get_feedback(db: Session, feedback_id: int):
    return (
        db.query(Feedback)
        .filter(Feedback.id == feedback_id)
        .first()
    )


def get_all_feedbacks(db: Session):
    return db.query(Feedback).all()


def delete_feedback(db: Session, feedback_id: int):
    feedback = (
        db.query(Feedback)
        .filter(Feedback.id == feedback_id)
        .first()
    )

    if feedback:
        db.delete(feedback)
        db.commit()

    return feedback