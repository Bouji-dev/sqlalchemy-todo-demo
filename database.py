from sqlalchemy import create_engine, MetaData

engine = create_engine('sqlite:///todo.db', echo=True)
metadata = MetaData()