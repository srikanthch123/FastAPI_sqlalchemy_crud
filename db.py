import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# Set up logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1234@localhost/todo_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        # Log a message indicating successful connection
        logging.info("Connected to database")
        yield db
    except Exception as e:
        # Log any exceptions that occur during connection
        logging.error("Error connecting to database: %s", e)
        raise
    finally:
        db.close()
