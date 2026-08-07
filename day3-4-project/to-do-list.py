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
        tasks = 