from sqlalchemy import select, insert, update, delete
from database import engine
from models_core import tasks


def add_task(title, description=None):
    with engine.connect() as conn:
        with conn.begin():
            result = conn.execute(
                insert(tasks).values(title=title, description=description)
            )
            conn.commit()
            return result.lastrowid


def list_tasks():
    with engine.connect() as conn:
        result = conn.execute(select(tasks))
        return result.fetchall()
    

def mark_completed(task_id):
    with engine.connect() as conn:
        with conn.begin():
            conn.execute(
                update(tasks)
                .where(tasks.c.id == task_id)
                .values(completed=True)
            )


def delete_task(task_id):
    with engine.connect() as conn:
        with conn.begin():
            conn.execute(
                delete(tasks)
                .where(tasks.c.id == task_id)
            )
