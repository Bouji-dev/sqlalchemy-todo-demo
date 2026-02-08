from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, DeclarativeBase


engine = create_engine('sqlite:///todo.db', echo=True)
metadata = MetaData()
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass