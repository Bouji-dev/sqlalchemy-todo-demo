from crud_orm import add_task, get_all_tasks
from database import SessionLocal

print("Day 6: ORM Quick Start")

with SessionLocal() as session:
    add_task(session, 'ORM Learning', 'So exciting')
    
    tasks = get_all_tasks(session)
    for task in tasks:
        print(f'ID: {task.id} | {task.title} | {task.completed}')



