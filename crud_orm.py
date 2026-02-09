from sqlalchemy.orm import Session
from models_orm import Task


def add_task(session: Session, title: str, description: str = None):
    task = Task(title=title, description=description)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

def get_all_tasks(session: Session):
    return session.query(Task).all()