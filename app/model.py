from sqlalchemy import Column, Integer, String,Boolean
from app.db import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email= Column(String)
    password = Column(String)


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    description = Column(String)
    is_bool=Column(Boolean) 