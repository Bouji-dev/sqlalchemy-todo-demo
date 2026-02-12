from database import SessionLocal
from crud_orm import get_pending_tasks


print("Day 10: Extensions & Best Practices")

with SessionLocal() as session:
    pending = get_pending_tasks(session)
    print(f"Number of Pending Tasks: {len(pending)}")
    for t in pending:
        print(t.title, t.status)
