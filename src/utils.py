from enum import Enum

class Role(Enum):
    Admin = 1
    Moderator = 2
    User = 3

class Status(Enum):
    Done = "done"
    Pending = "pending"