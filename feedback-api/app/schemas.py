from pydantic import BaseModel
from pydantic import EmailStr


class FeedbackCreate(BaseModel):
    user_name: str
    email: EmailStr
    message: str


class FeedbackResponse(FeedbackCreate):
    id: int

    class Config:
        from_attributes = True