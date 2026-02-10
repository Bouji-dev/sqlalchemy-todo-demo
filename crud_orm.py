from sqlalchemy.orm import Session
from models_orm import Task, User


def create_user(session: Session, username: str):
    user = User(username=username)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def add_task_to_user(session: Session, user: User, title: str, description: str = None):
    task = Task(title=title, description=description, user=user)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

def get_user_with_tasks(session: Session, user_id: int):
    return session.query(User).filter(User.id == user_id).first()