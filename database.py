from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, DeclarativeBase


engine = create_engine('sqlite:///todo.db', echo=True)

# for Core
metadata = MetaData()

# for ORM
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

# for ORM
class Base(DeclarativeBase):
    pass