# Import your classes (you will create these files)
from task import Task
from user import User
from utils import *


def main():
    print("=== PyTasks Demo ===")

    # Create users
    user = User("nikita", "nikita@kuzmin.com", "random_hash", Role.User)
    
    print(user)

    print("\n=== End of Demo ===")


# This ensures main() runs only when this file is executed directly
if __name__ == "__main__":
    main()
