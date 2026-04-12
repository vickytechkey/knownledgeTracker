from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base

DATABASE_URL = "sqlite:///./courses.db"

engine = create_engine(DATABASE_URL,connect_args={"check_same_threas":False})

SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)

base = declarative_base()