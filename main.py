from database import SessionLocal
from crud_orm import get_users_with_min_tasks, get_tasks_for_user

print("Day 8: Advanced ORM Querying")

with SessionLocal() as session:
    users = get_users_with_min_tasks(session)
    print("Users with minimum 2 tasks: ")
    for u in users:
        print(u.username, len(u.tasks))

    tasks = get_tasks_for_user(session, 1)
    print('\n User 1 tasks: ')
    for t in tasks:
        print(t.title)