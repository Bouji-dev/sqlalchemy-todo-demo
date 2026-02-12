from database import SessionLocal
from crud_orm import create_user_with_tasks

print("Day 9: Advanced Session & Transaction Management")

with SessionLocal() as session:
    try:
        user = create_user_with_tasks(
            session,
            'Ehsan',
            ['Study', 'Cooke', 'Play']
        )
        print(f'User : {user.username} with {len(user.tasks)} tasks created')

    except Exception as e:
        print(f'Error: {e}')

