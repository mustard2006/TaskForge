from task import Task
from user import User
from utils import *


def main():
    print("=== PyTasks Demo ===")

    # Create users
    user = User("user", "user@user.com", "random_hash", Role.User)
    user.load_tasks()  # Load saved tasks from JSON

    while True:
        print("\n1. Add task")
        print("2. Mark task done")
        print("3. List tasks")
        print("type 'bye' or 'exit' to quit")

        command = input(">>> ").strip().lower()

        if command == "bye" or command == "exit":
            user.save_tasks()  # Save before exiting
            print("Goodbye!")
            break

        elif command == "1":
            title = input("Enter title >>> ").strip().lower()
            desc = input("Enter description >>> ").strip().lower()

            task = Task(user.id, title, desc)
            user.add_task(task)
            user.save_tasks()
            print("Task added successfully!")
        
        elif command == "2":
            title = input("Enter task title to mark done >>> ").strip().lower()
            task = user.task_by_title(title)
            if task:
                task.mark_done()
                user.save_tasks()
                print(f"Task '{task.title}' marked done!")
            else:
                print("Task not found")
            
        elif command == "3":
            print("<=========== Task List ===========>")
            user.list_tasks()
            print("<=================================>")

        else:
            print("Invalid option")

    print("\n=== End of Demo ===")


# This ensures main() runs only when this file is executed directly
if __name__ == "__main__":
    main()
