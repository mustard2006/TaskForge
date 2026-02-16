from datetime import datetime
import uuid
from utils import *
from task import *
from typing import List

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
    
    # task methods
    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def remove_task(self, task) -> None:
        if task in self.tasks:
            self.tasks.remove(task)

    def list_tasks(self):
        for task in self.tasks:
            print(task)

    def task_by_id(self, task_id):
        return next((task for task in self.tasks if task.id == task_id), None)

    def task_by_title(self, title):
        return next((task for task in self.tasks if task.title == title), None)
    
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