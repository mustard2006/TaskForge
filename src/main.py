from task import Task
from user import User
from utils import *


def main():
    print("=== PyTasks Demo ===")

    # Create users
    user = User("nikita", "nikita@kuzmin.com", "random_hash", Role.User)
    
    # __str__
    #print(user)

    # __repr__
    #print(repr(user))

    task1 = Task(
        user_id=user.id,
        title="Homework",
        description="Complete math exercises by tomorrow"
    )
    user.add_task(task1)

    user.list_tasks()

    print("\n=== End of Demo ===")


# This ensures main() runs only when this file is executed directly
if __name__ == "__main__":
    main()
