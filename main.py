import todo
from datetime import datetime

def display_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task as Completed")
    print("4. List Tasks")
    print("5. Exit")

def main():
    tasks = todo.load_tasks()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            priority = input("Enter task priority (low, medium, high): ")
            due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ")
            due_date = due_date if due_date else None
            todo.add_task(tasks, description, priority, due_date)
        elif choice == '2':
            task_index = int(input("Enter task number to remove: ")) - 1
            todo.remove_task(tasks, task_index)
        elif choice == '3':
            task_index = int(input("Enter task number to mark as completed: ")) - 1
            todo.mark_task_completed(tasks, task_index)
        elif choice == '4':
            todo.list_tasks(tasks)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
