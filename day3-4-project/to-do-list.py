tasks = []
action = ""
def repeat_view():
    for i, item in enumerate(tasks):
        print(f"{i+1}. {item['task']} - Done: {item['done']}")
while action != "5":
    print("To-Do List")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark as done")
    print("4. Remove a task")
    print("5. Quit")
    action = input("Enter your action(1-5): ")
    if action == "1":
        more = "y"
        while more == "y":
            user_input = {}
            user_input ["task"] = input("Enter your tasks: ")
            user_input ["done"] = False
            tasks.append(user_input)
            more = input("do you want to add more tasks (y/n)?")
    elif action == "2":
        repeat_view()
    elif action == "3":
        repeat_view()
        done = int(input("which task you want to mark as done pick the order number (e.g. 1)"))
        marked_task = tasks[done-1]
        marked_task ["done"] = True
        repeat_view()
    elif action == "4":
        repeat_view()
        remove = int(input("here is your list of tasks, which one do you want to Mark As Done (type with number base on the order of the list you want to delete e.g. 1):"))
        removed_tasks = tasks.pop(remove - 1)
        repeat_view()
print("Goodbye")