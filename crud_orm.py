from sqlalchemy import select, func
from sqlalchemy.orm import Session
from models_orm import Task, User


def create_user_with_tasks(session: Session, username: str, task_titles: list[str]):
    try:
        user = User(username=username)
        session.add(user)
        session.flush()

        for title in task_titles:
            task = Task(title=title, user=user)
            session.add(task)
        
        session.commit()
        return user
    except Exception:
        session.rollback()
        raise


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


def get_users_with_min_tasks(session: Session, min_tasks: int = 2):
    stmt = (
        select(User)
        .join(Task)
        .group_by(User.id)
        .having(func.count(Task.id) >= min_tasks)
    )
    return session.scalars(stmt).all()


def get_tasks_for_user(session: Session, user_id: int):
    stmt = select(Task).where(Task.user_id == user_id)    
    return session.scalars(stmt).all()