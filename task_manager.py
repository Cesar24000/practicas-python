# Task Manager - Simple Version

def show_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks found yet!")

def add_task():
    task = input("Enter the new task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully!")

# Main loop to keep the program running
while True:
    print("\n--- TASK MANAGER ---")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        break
    else:
        print("Invalid option, try again.")