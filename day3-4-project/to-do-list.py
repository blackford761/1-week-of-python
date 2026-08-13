tasks = []
action = ""
while action != "5":
    print("To-Do List")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark task as complete")
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
        for i, item in enumerate(tasks):
            print(f"{i+1}. {item['task']} - Done {item['done']}")
    elif action == "3":
        remove = input(f"here is your list of tasks {tasks}, which one do you want to remove (type with number base on the order of the list you want to delete ex. 1, 3:)")
        removed_tasks = tasks.pop(remove)
        print (removed_tasks)