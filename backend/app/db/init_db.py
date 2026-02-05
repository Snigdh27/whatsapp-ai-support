from app.db.session import engine
from app.db.base import Base
from app.model.business import Business
from app.model.chat import Chat
from app.model.message import Message

def init():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init()