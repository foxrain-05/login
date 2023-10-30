from pydantic import EmailStr
from sqlmodel import Field, Session, SQLModel, create_engine


class User(SQLModel, table=True):
    email: EmailStr = Field(primary_key=True)
    username: str
    exp: int

engine = create_engine("sqlite:///database.db", echo=True)

def connect_db():
    SQLModel.metadata.create_all(engine)


    