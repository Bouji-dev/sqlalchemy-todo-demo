from crud_core import add_task, list_tasks, mark_completed, delete_task

print("Day 4: Core CRUD operations")

add_task('SQLAlchemy Exercise', 'Work with insert and delete')
add_task('Purchase', 'Egg and Milk')

print('\n Tasks list: ')
for task in list_tasks():
    print(task)

mark_completed(1)
delete_task(2)

# print('\n After changes: ')
# for task in list_tasks():
#     print(task)