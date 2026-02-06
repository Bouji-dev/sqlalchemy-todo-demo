from sqlalchemy import text
from database import engine


with engine.connect() as connection:
    connection.execute(text('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, title TEXT)'))
    connection.execute(text('INSERT INTO tasks (title) VALUES ("Sample Task")'))
    result = connection.execute(text('SELECT * FROM tasks'))
    print( result.fetchall())