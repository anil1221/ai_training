from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from app.database import Base


class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)

    user_name = Column(String(100), nullable=False)

    email = Column(String(150), nullable=False)

    message = Column(Text, nullable=False)