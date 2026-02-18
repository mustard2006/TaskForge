from datetime import datetime
import uuid
from utils import *
from task import *
from typing import List
import json
from pathlib import Path

TASKS_FILE = Path(__file__).parent / "tasks.json"

class User:
    def __init__(self, username, email, password_hash, role):
        self.id = uuid.uuid4()
        self._username = username
        self._email = email
        self.password_hash = password_hash
        self.tasks: List[Task] = []
        self.role: Role = role
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"User: username={self.username}, role={self.role.name}"

    def __repr__(self):
        return (f"User: id={self.id}, username={self.username}, password_hash={self.password_hash}, "
                f"email={self.email}, role={self.role.name}, tasks={self.tasks}, "
                f"created_at={self.created_at}, updated_at={self.updated_at}")
    
    def save_tasks(self):
        data = [task.to_dict() for task in self.tasks]
        with open(TASKS_FILE, "w") as f:
            return json.dump(data, f, indent=2)

    def load_tasks(self):
        try:
            with open(TASKS_FILE, "r") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(t) for t in data]
        except FileNotFoundError:
            self.tasks = []
        except json.JSONDecodeError:
            print("Corrupted file, starting fresh")
            self.tasks = []
        except PermissionError:
            print("Cannot read file - check permissions")
            raise

    # task methods
    def add_task(self, task: Task) -> None:
        task.title = task.title.lower()
        self.tasks.append(task)

    def remove_task(self, task) -> None:
        if task in self.tasks:
            self.tasks.remove(task)
    
    def list_tasks(self):
        if self.tasks:
            print(f"Total tasks: {len(self.tasks)}")
            for task in self.tasks:
                print(task)
        else:
            print("No tasks yet!")

    def task_by_id(self, task_id):
        return next((task for task in self.tasks if task.id == task_id), None)

    def task_by_title(self, title):
        title = title.lower()
        return next((task for task in self.tasks if task.title == title), None)

    #def save_tasks(self, filename="tasks.json"):   
    
    # username and email methods
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username) -> None:
        self._username = new_username
        self.updated_at = datetime.now()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email) -> None:
        self._email = new_email
        self.updated_at = datetime.now()

    # password methods
    def update_password(self, new_password_hash) -> None:
        self.password_hash = new_password_hash
        self.updated_at = datetime.now()