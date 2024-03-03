from sqlalchemy import Column, Integer, String
from db import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email= Column(String)
    password = Column(String)


class Tasks(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True,index=True)
    title = Column(String)
    description = Column(String)