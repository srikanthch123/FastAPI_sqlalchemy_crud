
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from fastapi import HTTPException
from dotenv import load_dotenv
import os
load_dotenv()

user_name = os.getenv('USER_NAME')
password = os.getenv("PASSWORD")
host = os.getenv( "HOST" )
db_name = os.getenv('DB_NAME')

SQLALCHEMY_DATABASE_URL = f"postgresql://{user_name}:{password}@{host}/{db_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        # Log a message indicating successful connectio
        yield db
    except Exception as e:
        raise HTTPException(e)
    finally:
        db.close()
