def add_task(task):
    if task not in toDoList:
        toDoList.append(task)
        print("Task added successfully")
    else:
        print("Task already added")


def check_if_exist(task):
    return task in toDoList


def remove_task(task):
    if check_if_exist(task):
        toDoList.remove(task)
        print("Task removed successfully")
    else:
        print("Task not found")


def view_all_tasks():
    count = 1
    print("******My Tasks******")
    for task in toDoList:
        print(f"{count}. {task}")
        count = count + 1


print("******TO DO LIST MANAGER******")

toDoList = []

print("What do you want to do? 1 = add tasks || 2 = remove tasks || 3 = view added tasks || 0 = End")
user_action = int(input(">>>"))

while user_action != 0:
    #add task
    if user_action == 1:
        task = input("Enter task to add")
        add_task(task)
    #remove task
    elif user_action == 2:
        if len(toDoList) != 0:
            task = input("Enter name of task to remove: ")
            remove_task(task)
        else:
            print("Add a task first")
    #view tasks
    elif user_action == 3:
        view_all_tasks()

    else:
        pass

    print("What do you want to do? 1 = add tasks || 2 = remove tasks || 3 = view added tasks || 0 = End")
    user_action = int(input(">>>"))

