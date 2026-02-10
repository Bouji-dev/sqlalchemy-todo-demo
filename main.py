from database import SessionLocal
from crud_orm import create_user, add_task_to_user, get_user_with_tasks

print("Day 7: Relationships in ORM")

with SessionLocal() as session:
    user = create_user(session, "sara")
    add_task_to_user(session, user, "خرید", "شیر و نان")
    add_task_to_user(session, user, "تمرین", "SQLAlchemy")

    loaded_user = get_user_with_tasks(session, user.id)
    print(f"کاربر: {loaded_user.username}")
    for t in loaded_user.tasks:
        print(f"  تسک: {t.title}")