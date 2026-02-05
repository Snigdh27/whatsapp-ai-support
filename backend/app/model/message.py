from sqlalchemy import Column, Integer, String, ForeignKey, Text
from app.db.base import Base

class Message(Base):
    __tablename__ = "messages"

    id= Column(Integer, primary_key=True, index=True)
    chat_id = Column(Integer, ForeignKey("chats.id"))
    sender = Column(String)
    content = Column(Text)