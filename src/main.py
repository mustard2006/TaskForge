from crud import *
from utils import *
from database import SessionLocal, engine, Base
from models import User, Task

def main():
    Base.metadata.create_all(bind=engine) # create tables
    db = SessionLocal()

    # Get or create user
    user = get_user_by_username(db, "user")
    if not user:
        user = create_user(db, "user", "user@gmail.com", "random_hash", Role.User)

    print("=== PyTasks Demo ===")

    while True:
        print("\n1. Add task")
        print("2. Mark task done")
        print("3. List tasks")
        print("type 'bye' or 'exit' to quit")

        command = input(">>> ").strip().lower()

        if command == "bye" or command == "exit":
            
            print("Goodbye!")
            break

        elif command == "1":
            title = input("Enter title >>> ").strip().lower()
            desc = input("Enter description >>> ").strip().lower()

            task = create_task(db, title, desc, user.id)
            
            print("Task added successfully!")
        
        elif command == "2":
            title = input("Enter task title to mark done >>> ").strip().lower()
            task = mark_task_done(db, title)
            if task:
                print(f"Task '{task.title}' marked done!")
            else:
                print("Task not found")
            
        elif command == "3":
            print("<=========== Task List ===========>")
            tasks = get_tasks(db, user.id)
            if tasks:
                for t in tasks:
                    print(t)
            else:
                print("No tasks yet!")
            print("<=================================>")

        else:
            print("Invalid option")

    print("\n=== End of Demo ===")

    db.close()

# This ensures main() runs only when this file is executed directly
if __name__ == "__main__":
    main()
